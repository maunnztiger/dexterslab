document.addEventListener('DOMContentLoaded', () => {
  // --- Config / LocalStorage ---
  const tableName = localStorage.getItem('tableName') || 'data_general';
  const headlineValue = localStorage.getItem('linkText') || '';
  const headlineEl = document.getElementById('headline');
  const titleEl = document.querySelector('title');
  if (headlineEl) headlineEl.textContent = headlineValue;
  if (titleEl) titleEl.textContent = headlineValue;

  // --- DataTable-Instanz (wird später gesetzt) ---
  let dataTableInstance = null;
  let currentParam = null; // für setParameter/getParameter

  // --- Fetch initial data und DataTable initialisieren ---
  fetch(`/data/${encodeURIComponent(tableName)}`, {
    method: 'GET',
    headers: { 'Accept': 'application/json' }
  })
    .then(res => res.json())
    .then(data => {
      const tableEl = document.querySelector('table');
      const tableId = tableEl ? tableEl.id : 'mytable';

      // jQuery DataTables Initialisierung und Instanz speichern
      dataTableInstance = $('#' + tableId).DataTable({
        autoWidth: false,
        destroy: true,
        pageLength: 50,
        columnDefs: [{ targets: ['_all'], className: 'mdc-data-table__cell' }],
        data: data,
        columns: [
          { title: 'Id', data: 'id' },
          { title: 'Aspekt', data: 'aspect' },
          { title: 'Value', data: 'value' },
          { data: null, className: 'dt-center editor-edit', defaultContent: '<i class="fa fa-pencil"/>', orderable: false },
          { data: null, className: 'dt-center editor-delete', defaultContent: '<button><i class="fa fa-trash"/></button>', orderable: false }
        ]
      });

      // Edit handler (delegation)
      $('#' + tableId).on('click', 'td.editor-edit', function (e) {
        e.preventDefault();
        const datatableIndex = $(this).closest('tr').find('td').first().text();
        setParameter(datatableIndex);
        openUpdateEditor(datatableIndex);
      });

      // Delete handler (delegation)
      $('#' + tableId).on('click', 'td.editor-delete', function (e) {
        e.preventDefault();
        const datatableIndex = $(this).closest('tr').find('td').first().text();
        setParameter(datatableIndex);
        if (confirm("You really want to delete this row?!\nEither OK or Cancel.")) {
          deleteRow(datatableIndex);
        }
      });
    })
    .catch(err => {
      console.error('Fetch error', err);
    });

  // --- Exponierte Wrapper (falls HTML Inline-Handler benutzt) ---
  window.createRecord = function () { createRecord(); };
  window.deleteRow = function (id) { deleteRow(id); };
  window.saveChanges = function () { saveChanges(); };
  window.openCreateEditor = openCreateEditor;
  window.openUpdateEditor = openUpdateEditor;
  window.closeCreateEditor = closeCreateEditor;
  window.closeEditor = closeEditor;

  // ===========================
  // Editor / CRUD Funktionen
  // ===========================

  function openUpdateEditor(id) {
    // Suche Zeile per id in DataTable und fülle Felder
    if (!dataTableInstance) { console.warn('DataTable not ready'); return; }
    let found = null;
    dataTableInstance.rows().every(function () {
      const rowData = this.data();
      if (String(rowData.id) === String(id)) {
        found = rowData;
      }
    });
    if (!found) {
      alert('Row not found: ' + id);
      return;
    }
    const aspectInput = document.getElementById('aspect');
    const valueInput = document.getElementById('value');
    if (aspectInput) aspectInput.value = found.aspect || '';
    if (valueInput) valueInput.value = found.value || '';

    document.getElementById('popup').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';
  }

  function openCreateEditor() {
    document.getElementById('popup2').style.display = 'block';
    document.getElementById('overlay2').style.display = 'block';
  }

  function closeEditor() {
    const p = document.getElementById('popup');
    const o = document.getElementById('overlay');
    if (p) p.style.display = 'none';
    if (o) o.style.display = 'none';
  }

  function closeCreateEditor() {
    const p = document.getElementById('popup2');
    const o = document.getElementById('overlay2');
    if (p) p.style.display = 'none';
    if (o) o.style.display = 'none';
  }

  function createRecord() {
    const idInput = document.getElementById('Id');
    const aspectInput = document.getElementById('aspect2');
    const valueInput = document.getElementById('value2');
    const id = idInput ? idInput.value.trim() : '';
    const aspect = aspectInput ? aspectInput.value : '';
    const value = valueInput ? valueInput.value : '';

    const payload = { table_name: tableName, aspect: aspect, value: value };
    if (id !== '') payload.index = id; // optional: send index only when filled

    $.ajax({
      type: "POST",
      url: 'insert_row',
      data: JSON.stringify(payload),
      contentType: 'application/json; charset=utf-8',
      dataType: 'json',
      success: function (response) {
        console.log('insert response', response);
        if (response && response.success && response.new_row && dataTableInstance) {
          // new_row is expected to be an object {id, aspect, value}
          dataTableInstance.row.add(response.new_row).draw(false);
        }
        if (idInput) idInput.value = '';
        if (aspectInput) aspectInput.value = '';
        if (valueInput) valueInput.value = '';
        closeCreateEditor();
      },
      error: function (xhr, status, err) {
        console.error('Insert failed', status, err, xhr && xhr.responseText);
        alert('Insert failed: ' + status);
      }
    });
  }

  function saveChanges() {
    const datatableIndex = getParameter();
    const aspectInput = document.getElementById('aspect');
    const valueInput = document.getElementById('value');
    const newAspect = aspectInput ? aspectInput.value : '';
    const newValue = valueInput ? valueInput.value : '';

    const payload = {
      table_name: tableName,
      id: datatableIndex,
      newAspect: newAspect,
      newValue: newValue
    };

    $.ajax({
      type: "POST",
      url: 'update_row',
      data: JSON.stringify(payload),
      contentType: 'application/json; charset=utf-8',
      dataType: 'json',
      success: function (response) {
        console.log('update response', response);
        if (response && response.success && dataTableInstance) {
          // Update table rows that match id
          dataTableInstance.rows().every(function () {
            const rowData = this.data();
            if (String(rowData.id) === String(datatableIndex)) {
              // Prefer server-returned updated row if available
              const updated = response.updated_row || { id: datatableIndex, aspect: newAspect, value: newValue };
              this.data(updated);
            }
          });
          dataTableInstance.draw(false);
        }
        closeEditor();
      },
      error: function (xhr, status, err) {
        console.error('Update failed', status, err, xhr && xhr.responseText);
        alert('Update failed: ' + status);
      }
    });
  }

  function deleteRow(datatableIndex) {
    const payload = { id: datatableIndex, table_name: tableName };

    $.ajax({
      type: "POST",
      url: 'delete_row',
      data: JSON.stringify(payload),
      contentType: 'application/json; charset=utf-8',
      dataType: 'json',
      success: function (response) {
        console.log('delete response', response);
        if (response && response.success && dataTableInstance) {
          // remove matching rows
          dataTableInstance.rows().every(function () {
            const rowData = this.data();
            if (String(rowData.id) === String(datatableIndex)) {
              this.remove();
            }
          });
          dataTableInstance.draw(false);
        }
      },
      error: function (xhr, status, err) {
        console.error('Delete failed', status, err, xhr && xhr.responseText);
        alert('Delete failed: ' + status);
      }
    });
  }

  // Utility parameter getters/setters
  function setParameter(param) {
    currentParam = param;
  }

  function getParameter() {
    return currentParam;
  }

  // Misc helpers
window.goBack = function() {
  if (document.referrer && document.referrer !== window.location.href) {
    window.location.href = document.referrer;
  } else {
    window.location.href = "/index.html"; // Fallback
  }
};


  function openDiagramPage() {
    location.assign('diagram.html');
  }
});

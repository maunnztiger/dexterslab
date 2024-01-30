 fetch('http://localhost:8080/general_data',{
            method: 'GET',
       })
      .then(response => response.json())    
      .then(data => {
      
        const table = new DataTable('#table_raw', {
        autoWidth: true,
        columnDefs: [
          {
              targets: ['_all'],
              className: 'mdc-data-table__cell',
          },
        ],
        data: data,
        columns: [
          { title: 'Id', data: 'general_id'},
          { title: 'Aspekt', data: 'aspect'},
          { title: 'Value', data: 'value'},
          {
            data: null,
            className: 'dt-center editor-edit',
            defaultContent: '<i class="fa fa-pencil"/>',
            orderable: false
        },
        {
            data: null,
            className: 'dt-center editor-delete',
            defaultContent: '<i class="fa fa-trash"/>',
            orderable: false
        }
          
        ],
      });

      // Edit record
      $('#table_raw tr').on('click', 'td.editor-edit', function (e) {
      e.preventDefault();
      let templteIndex = $(this).closest('tr').index();
      console.log(templteIndex); 
      openEditor(templteIndex+1);
      });
}) 
function goBack() {
  window.history.back();
}

  const newChild = document.getElementById("menuButton")
  const parentElement = document.body

  parentElement.insertBefore(newChild, parentElement.firstChild);
  function openEditor(index){// Get data from the selected row
    var table = document.getElementById('table_raw');
    var nameInput = document.getElementById('aspect');
    var emailInput = document.getElementById('value');
    var selectedRow = table.rows[index];
    var aspect = selectedRow.cells[1].innerHTML;
    var value = selectedRow.cells[2].innerHTML;

    // Populate the editor with the selected data
    nameInput.value = aspect;
    emailInput.value = value;

    // Show the popup and overlay
    document.getElementById('popup').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';

  }

  function closeEditor() {
    // Hide the popup and overlay
    document.getElementById('popup').style.display = 'none';
    document.getElementById('overlay').style.display = 'none';
}

  function saveChanges() {
    var aspectInput = document.getElementById('aspect');
    var valueInput = document.getElementById('value');

    // Get the edited data
    var newAspect = aspectInput.value;
    var newValue = valueInput.value;
    const obj = {};
    obj.newAspect = newAspect;
    obj.newValue = newValue;
    const data = JSON.stringify({obj});

    $.ajax({
      type: "POST",
      url: 'general_data_update_row',
      data: data,
      success: function (response) {
        console.log(response);
      },
      headers: {
      'Content-type':'application/json', 
      'Accept':'application/json'
      },
      dataType: "application/json; charset=utf-8"
    })
    // Close the editor
    closeEditor();
}
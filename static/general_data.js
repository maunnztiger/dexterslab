  fetch('http://localhost:8080/general_data',{
            method: 'GET',
       })
      .then(response => response.json())    
      .then(data => {
      
        const table = new DataTable('#data_general', {
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
          { title: 'Von den Befragten, die Homeoffice machen', data: 'aspect'},
          { title: 'Wert in Prozent', data: 'value'},
          {
            data: null,
            className: 'dt-center editor-edit',
            defaultContent: '<i class="fa fa-pencil"/>',
            orderable: false,
          },
          {
            data: null,
            className: 'dt-center editor-delete',
            defaultContent: '<button><i class="fa fa-trash"/></button>',
            orderable: false
        }
        ],        
      });

      // Edit record
      $('#data_general').on('click', 'td.editor-edit', function (e) {
      e.preventDefault();
      let templateIndex = $(this).closest('tr').index();
      let datatableIndex = $(this).closest('tr').find('td').first().text();
      setParameter(datatableIndex);
      console.log(templateIndex); 
      
      openUpdateEditor(templateIndex+1);
      });

      $('#data_general').on('click', 'td.editor-delete', function (e) {
        e.preventDefault();
        let datatableIndex = $(this).closest('tr').find('td').first().text();
        setParameter(datatableIndex);
        if(confirm("You really want to delete this row?!\nEither OK or Cancel.")){
          deleteRow(datatableIndex);
        }
        
        });


  }); 

  const newChild = document.getElementById("menuButton")
  const parentElement = document.body
  parentElement.insertBefore(newChild, parentElement.firstChild);

  function openUpdateEditor(index){
    var table = document.getElementById('data_general');
    var aspectInput = document.getElementById('aspect');
    var valueInput = document.getElementById('value');
    var selectedRow = table.rows[index];
    var aspect = selectedRow.cells[1].innerHTML;
    var value = selectedRow.cells[2].innerHTML;

    
    aspectInput.value = aspect;
    valueInput.value = value;

    // Show the popup and overlay
    document.getElementById('popup').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';
  }

  function openCreateEditor(){
    let elementName = document.getElementById('data_general')
    console.log(elementName.id)
    document.getElementById('popup2').style.display = 'block';
    document.getElementById('overlay2').style.display = 'block';
  }

  function closeEditor() {
    // Hide the popup and overlay
    document.getElementById('popup').style.display = 'none';
    document.getElementById('overlay').style.display = 'none';

  }

  function closeCreateEditor() {
    // Hide the popup and overlay
    document.getElementById('popup2').style.display = 'none';
    document.getElementById('overlay2').style.display = 'none';

  }

  function createRecord(){
    let elementName = document.getElementById('data_general')
    console.log(elementName.id)
    let idInput = document.getElementById('Id');
    let aspectInput = document.getElementById('aspect2');
    let valueInput = document.getElementById('value2');
      // Get the edited data

    let id = idInput.value;
    let aspect = aspectInput.value;
    let value = valueInput.value;

    this.obj = {};
    this.obj.table_name = elementName.id
    this.obj.index = id;
    this.obj.aspect = aspect;
    this.obj.value = value;
    const data = JSON.stringify(this.obj);
    console.log(this.obj)
    $.ajax({
      type: "POST",
      url: 'insert_row',
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
    closeCreateEditor();
    setTimeout(function(){
      window.location.reload(location.href);
   }, 500);
  }

  function saveChanges() {
    let elementName = document.getElementById('data_general')
    console.log(elementName.id)
    let aspectInput = document.getElementById('aspect');
    let valueInput = document.getElementById('value');
      // Get the edited data

    let newAspect = aspectInput.value;
    let newValue = valueInput.value;
    
    datatableIndex = this.getParameter();
    this.obj = {};
    this.obj.table_name = elementName.id
    this.obj.datatableIndex = datatableIndex;
    this.obj.newAspect = newAspect;
    this.obj.newValue = newValue;
    const data = JSON.stringify(this.obj);
    console.log(this.obj)
    $.ajax({
      type: "POST",
      url: 'update_row',
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
    setTimeout(function(){
      window.location.reload(location.href);
   }, 500);
  }

  function deleteRow(datatableIndex){
    let elementName = document.getElementById('data_general')
    console.log(elementName.id, datatableIndex)
    this.obj = {};
    this.obj.id = datatableIndex;
    this.obj.table_name = elementName.id;
    const data = JSON.stringify(this.obj);
    $.ajax({
      type: "POST",
      url: 'delete_row',
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
    setTimeout(function(){
      window.location.reload(location.href);
    }, 500);
   
  }

  function setParameter(param) {
    this.param = param;
  }

  function getParameter(){
    return this.param;
  }

  function goBack() {
    window.history.back();
  }
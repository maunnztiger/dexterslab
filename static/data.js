let table_name = document.getElementsByTagName('table')[0].id
  fetch('http://www.dexterslab.com:8080/data/'+table_name,{
            method: 'GET',
            headers: {
              'Content-type':'application/json', 
              'Accept':'application/json'
              },
              dataType: "application/json; charset=utf-8"
       })
      .then(response => response.json())    
      .then(data => {
        let table_name = document.getElementsByTagName('table')[0].id
        const table = new DataTable('#'+table_name, {
        autoWidth: false,
        pageLength: 50,     
        columnDefs: [
          {
              targets: ['_all'],
              className: 'mdc-data-table__cell',
          },
        ],
        data: data,
        columns: [
          { title: 'Id', data: 'id'},
          { title: 'Aspekt', data: 'aspect'},
          { title: 'Value', data: 'value'},
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

        
        console.log(table_name)
        // Edit record
        $('#'+table_name).on('click', 'td.editor-edit', function (e) {
        e.preventDefault();
        let templateIndex = $(this).closest('tr').index();
        let datatableIndex = $(this).closest('tr').find('td').first().text();
        setParameter(datatableIndex);
        console.log(templateIndex); 
      
        openUpdateEditor(templateIndex+1);
        });

        // Delete Record
        $('#'+table_name).on('click', 'td.editor-delete', function (e) {
        e.preventDefault();
        let datatableIndex = $(this).closest('tr').find('td').first().text();
        setParameter(datatableIndex);
        if(confirm("You really want to delete this row?!\nEither OK or Cancel.")){
          deleteRow(datatableIndex);
        }
        
        });
    }); 

  const newChild = document.getElementById("returnButton")
  const parentElement = document.body
  parentElement.insertBefore(newChild, parentElement.firstChild);

  function openUpdateEditor(index){
    let table_name = document.getElementsByTagName('table')[0].id
    var table = document.getElementById(table_name);
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
    document.getElementById('popup2').style.display = 'block';
    document.getElementById('overlay2').style.display = 'block';
  }

  function closeEditor() {
    // Hide the popup and overlay
    document.getElementById('popup').style.display = 'none';
    document.getElementById('overlay').style.display = 'none';
  }

  function closeCreateEditor() {
    document.getElementById('popup2').style.display = 'none';
    document.getElementById('overlay2').style.display = 'none';
  }

  function createRecord(){
    let table_name = document.getElementsByTagName('table')[0].id
    console.log(table_name)
    let idInput = document.getElementById('Id');
    let aspectInput = document.getElementById('aspect2');
    let valueInput = document.getElementById('value2');
    let id = idInput.value;
    let aspect = aspectInput.value;
    let value = valueInput.value;

    this.obj = {};
    this.obj.table_name = table_name
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
    let table_name = document.getElementsByTagName('table')[0].id
    console.log(table_name)
    let aspectInput = document.getElementById('aspect');
    let valueInput = document.getElementById('value');
    let newAspect = aspectInput.value;
    let newValue = valueInput.value;
    
    datatableIndex = this.getParameter();
    this.obj = {};
    this.obj.table_name = table_name
    this.obj.datatableIndex = datatableIndex;
    this.obj.newAspect = newAspect;
    this.obj.newValue = newValue;
    const data = JSON.stringify(this.obj);
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
   closeEditor();
   setTimeout(function(){
     window.location.reload(location.href);
   }, 500);
  }

  function deleteRow(datatableIndex){
    let table_name = document.getElementsByTagName('table')[0].id
    console.log(table_name)
    this.obj = {};
    this.obj.id = datatableIndex;
    this.obj.table_name = table_name;
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

  function openDiagramPage(){
    console.log('graph.js')
    location.assign('diagram.html')
  }
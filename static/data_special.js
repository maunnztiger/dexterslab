fetch('http://localhost:8080/data_special',{
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
          { title: 'Id', data: 'special_id'},
          { title: 'Von den Angestellten, die Homeoffice machen', data: 'aspect'},
          { title: 'Wert in Prozent', data: 'value'},
        ],
      });
 }); 

 function goBack() {
  window.history.back();
}
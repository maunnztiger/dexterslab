fetch('http://localhost:8080/men_data',{
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
          { title: 'Id', data: 'men_id'},
          { title: 'Männer, die Homeoffice machen', data: 'aspect'},
          { title: 'Wert in Prozent', data: 'value'},
        ],
      });
 }); 

 function goBack() {
  window.history.back();
}
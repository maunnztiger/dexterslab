 fetch('http://localhost:8080/general_data',{
            method: 'GET',
       })
      .then(response => response.json())    
      .then(data => {
        new DataTable('#table_raw', {
        autoWidth: false,
        columnDefs: [
          {
              targets: ['_all'],
              className: 'mdc-data-table__cell',
          },
        ],
        data: data,
        columns: [
          { title: 'ID' , data: 'general_id'},
          { title: 'Aspekt der Umfrage' ,data: 'aspect'},
          { title: 'Zahlen in %' ,data: 'value'},
        ],
      })
     }) 

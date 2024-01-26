 fetch('http://localhost:8080/general_data',{
            method: 'GET',
       })
      .then(response => response.json())    
      .then(data => {
        console.log(data)
        new DataTable('#table_raw', {
        autoWidth: true,
        columnDefs: [
          {
              targets: ['_all'],
              className: 'mdc-data-table__cell',
          },
        ],
        data: data,
        columns: [
          { title: 'Aspekt der Umfrage' ,data: 'aspect'},
          { title: 'Zahlen in %' ,data: 'value'},
        ],
      })
     }) 
console.log('data')

function goBack() {
  window.history.back();
  }

  const newChild = document.getElementById("menuButton")
  const parentElement = document.body

  parentElement.insertBefore(newChild, parentElement.firstChild);
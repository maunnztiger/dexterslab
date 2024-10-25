fetch('https://192.168.178.54:5000/data/data_diagram',{
            method: 'GET',
       })
      .then(response => response.json())    
      .then(data => {            
        const ctx = document.getElementById('myChart');
  
        const chart = new Chart(ctx, {
            type: 'bar',
            data: {
            labels: data.map(row =>row.aspect),
            datasets: [{
                label: 'Homeoffice in Germany and other countries in Europe',
                data: data.map(row=>parseInt(row.value.slice(0, -1))),
                borderWidth: 2,
                indexAxis: 'x'
                }]
            },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                 }
            },
        interaction: {
            mode: 'index'
        },
        plugins: {
            customCanvasBackgroundColor: {
              color: 'lightGreen',
            },
            decimation: 'lttb',
        }
      }
    });
    chart.canvas.parentNode.style.height = '62%';
    chart.canvas.parentNode.style.width = '75%'; 
    chart.canvas.parentNode.style.top = '15%'; 
    chart.canvas.parentNode.style.left = '15%'; 
    chart.canvas.parentNode.style.position = 'absolute'; 
    
      })
console.log("Jenkins_fuckoff_")
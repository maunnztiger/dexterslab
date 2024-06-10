fetch('http://www.dexterslab.com:8080/video_source',{
    method: 'GET',
    headers: {
      'Content-type':'application/json', 
      'Accept':'application/json'
      },
      dataType: "application/json; charset=utf-8"
})
.then(response => response.json())    
.then(data => { 

    console.log(data)
})





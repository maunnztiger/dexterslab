fetch('http://192.168.178.53:8080/video_source',{
    method: 'GET',
    headers: {
      'Content-type':'application/json', 
      'Accept':'application/json'
      },
      dataType: "application/json; charset=utf-8"
})
.then(response => response.json())    
.then(data => { 

    console.log(data[0]['video_source']);
    src = data[0]['video_source'];
    const iframe = document.querySelector('iframe');
    iframe.setAttribute('src', src);


})
window.addEventListener('beforeunload', function(e) {
    this.obj = {};
    this.obj.id = 0;
    this.obj.table_name = 'video_source';
    const data = JSON.stringify(this.obj);
    console.log(this.obj)
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
    
  });


const links = document.getElementsByTagName('img')
for(const element of links){
    
    console.log(element.id)
    $("#"+ element.id).on('click', function (e) {  
        e.preventDefault();
        this.obj = {};
        this.obj.index = element.id
        const data = JSON.stringify(this.obj);
        console.log(this.obj)
        $.ajax({
          type: "POST",
          url: 'video_source',
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
        setTimeout(() => {  window.location.assign("video_source.html"); }, 2000);
        
    })
}


function goToHomePage(){
  window.location.assign("index.html");
}
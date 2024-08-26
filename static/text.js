const links = document.getElementsByTagName('img')
const image_container = document.getElementById('image_container')
let text_list_button = document.getElementById('text_list').style.display ='none'
const iframe_container = document.getElementById('iframe_container').style.display='none'

for(const element of links){
    
    console.log(element.id)
    $("#"+element.id).click(function(){  
        
      document.getElementById('image_container').style.display ='none';
      document.getElementById('main_menu').style.display ='none';
      document.getElementById('iframe_container').style.display ='block';
      let src = element.getAttribute("data-text-resource")
      const iframe = document.querySelector('iframe');
      iframe.setAttribute('src', src);
      let slide_list_button = document.getElementById('text_list');
      slide_list_button.style.display = 'block';
      
      $("#text_list").click(function(){ 
        document.getElementById('iframe_container').style.display ='none';  
        document.getElementById('text_list').style.display = 'none';
        document.getElementById('image_container').style.display='block'
        document.getElementById('main_menu').style.display ='block';
      })
    })
}

function goToHomePage(){
    window.location.assign("index.html");
  }
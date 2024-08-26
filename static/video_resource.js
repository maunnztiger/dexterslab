const links = document.getElementsByTagName('img')
const link_container = document.getElementById('link_container')
let video_list = document.getElementById('video_list').style.display ='none'
const iframe_container = document.getElementById('video_container').style.display='none'


for(const element of links){
    
    console.log(element.id)
    $("#"+element.id).click(function(){  
        
      document.getElementById('video_container').style.display ='block';
      link_container.style.display = 'none';
      let src = element.getAttribute("data-video-source")
      const iframe = document.querySelector('iframe');
      iframe.setAttribute('src', src);
      let video_list = document.getElementById('video_list');
      video_list.style.display = 'block';
      $("#video_list").click(function(){ 
          document.getElementById('video_container').style.display='none'
          document.getElementById('link_container').style.display ='block';
          document.getElementById('video_list').style.display = 'none';
          document.getElementById('main_menu').style.display ='block';

      })
      })


}




function goToHomePage(){
  window.location.assign("index.html");
}
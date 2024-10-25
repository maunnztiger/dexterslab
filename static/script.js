function toggleMenu() {
    let menu = document.getElementById('menu');
    let menuButton = document.getElementById('menuButton');
    if (menu.style.left === '0px') {
        menu.style.left = '-250px';
        menuButton.style.left = '280px'
    } else {
        menu.style.left = '0px';
        menuButton.style.left = '35px'
        menuButton.style.padding = '10px 30px';
    }
}
    
function openCreateEditor(){
    document.getElementById('popup').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';
}

function closeEditor() {
    // Hide the popup and overlay
    document.getElementById('popup').style.display = 'none';
    document.getElementById('overlay').style.display = 'none';
}
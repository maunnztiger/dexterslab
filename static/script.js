function toggleMenu() {
    let menu = document.getElementById('menu');
    let menuButton = document.getElementById('menuButton');
    if (menu.style.left === '0px') {
        menu.style.left = '-250px';
        menuButton.style.left = '270px'
    } else {
        menu.style.left = '0px';
        menuButton.style.left = '10px'
        menuButton.style.padding = '10px 20px';
    }
}

console.log('menu');
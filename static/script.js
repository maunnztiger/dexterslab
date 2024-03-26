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
  let table_name = document.getElementsByTagName('a')[0].id  ;
  console.log(table_name);
 $('#' + table_name).on('click', function (e) {
    e.preventDefault();
    this.obj = {};
    this.obj.table_name = table_name
    const data = JSON.stringify(this.obj);
    console.log(data)
        
 });
    
    
  
  
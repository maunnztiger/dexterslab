function openUserEditor(){
    document.getElementById('add_user').style.display = 'block';
}
function closeUserEditor() {
    // Hide the popup and overlay
    document.getElementById('add_user').style.display = 'none';
}


function saveUser() {
    const table_name = localStorage.table_name
    console.log(table_name)
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    const username= usernameInput.value;
    const password = passwordInput.value;
    
    this.obj = {};
    this.obj.table_name = 'users'
    this.obj.username = username;
    this.obj.password = password;
    const data = JSON.stringify(this.obj);
    $.ajax({
      type: "POST",
      url: 'add_new_user',
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
   closeUserEditor()();
  }
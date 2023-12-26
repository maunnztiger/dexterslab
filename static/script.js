class Model {
  getData(callback){
    fetch('http://localhost:8080/getData',{
            method: 'GET',
       })
      .then(response => response.json())    
      .then(data =>
      callback(data));
      }

       

  }
  
  class View {
    // Create an element with an optional CSS class
  createElement(tag, className) {
    const element = document.createElement(tag)
    if (className) element.classList.add(className)
      return element
    }
  
  // Retrieve an element from the DOM
  getElement(selector) {
    const element = document.querySelector(selector);
    return element;
  }
  
  displayData(data){
    console.log("displayed", data);
    if (data.length === 0) {
      const p = this.createElement('p');
      p.textContent = 'No Data passed!';
      this.commandList.append(p);
    } else {

        


    }
 }
}

  
  
  class Controller {
  constructor(model, view) {
    this.model = model;
    this.view = view;
    var obj = this;
    this.model.getData(function(data){
      obj.view.displayData(data);
    });
  }
 }
  
  const app = new Controller(new Model(),new View() );
         
         
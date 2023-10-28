import model
import view
import controller
import data

def main():
   
    c = controller.Controller(model.ModelBasic(data.my_items), view.View)   
    c.show_items(bullet_points=False)
    

if __name__ == '__main__':
    main()

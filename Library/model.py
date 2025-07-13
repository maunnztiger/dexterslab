from . import basic_backend
  
def read_data(table_name):
        result = basic_backend.read_data(table_name) 
        return result
   
def update_data(table_name, newAsepct, newValue , id):
        basic_backend.update_data(table_name, newAsepct, newValue, id)
        
def insert_data(table_name, newid, newaspect, newvalue):
        basic_backend.insert_data(table_name, newid, newaspect, newvalue)

def delete_row(id, table_name):
        basic_backend.delete_row(id, table_name)

def add_new_user(username, password):
        basic_backend.add_user(username, password)
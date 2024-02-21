from . import basic_backend
  
def read_data_general():
        result = basic_backend.read_data_general() 
        return result

def read_men_data():
        result = basic_backend.read_men_data()
        return result

def read_special_data():
        result = basic_backend.read_special_data()
        return result
    
def update_data(table_name, newAsepct, newValue , id):
        basic_backend.update_data(table_name, newAsepct, newValue, id)
        
def insert_data(table_name, id, aspect, value):
        basic_backend.insert_data(table_name, id, aspect, value)

def delete_row(id, table_name):
        basic_backend.delete_row(id, table_name)        
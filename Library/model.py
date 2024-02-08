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
    
def update_data_general(table_name, newAsepct, newValue , id):
        basic_backend.update_data_general(table_name, newAsepct, newValue, id)
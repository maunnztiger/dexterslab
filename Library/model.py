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

def insert_video_source(index):
        result = basic_backend.read_video_json(index)
        basic_backend.insert_video_src(result)
        
def read_video_source_data():
        result = basic_backend.read_video_source_data()
        return result

def delete_video_source():
        basic_backend.delete_video_source(0, 'video_source')
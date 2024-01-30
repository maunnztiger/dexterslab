from sqlalchemy import create_engine,  text
from sqlalchemy.orm import sessionmaker
from decimal import Decimal
from . import query_builder as model
import json

user = 'postgres'
password = 'root'  
host = 'localhost'
port = '5432'
database = 'testdb'

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return str(o)
        return super().default(o)

def connect_to_database():
    connection_str = f'postgresql://{user}:{password}@{host}:{port}/{database}'        
    engine = create_engine(connection_str)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def read_items():
    session = connect_to_database()
    query_builder = model.QueryBuilder('data_general') 
    query = query_builder.select('general_id', 'aspect', 'value').build() 
    result= session.execute(text(query))
    json_array = json.dumps([row._asdict() for row in result.fetchall()],  cls=DecimalEncoder, ensure_ascii=False).encode('utf-8')
    session.close()
    # print (json_array)
    return json_array

def read_item(name):
    global items
    
def create_items(app_items):
    global items
    items = app_items
    
def create_item(name, price, quantity):
    global items
   
    
def update_item(name, price, quantity):
    global items
    

def delete_item(name):
    global items
   

        

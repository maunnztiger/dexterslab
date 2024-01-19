from sqlalchemy import create_engine,  text
from sqlalchemy.orm import sessionmaker
from decimal import Decimal
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

def read_items():
    # Verbindung zur Datenbak herstellen
    connection_str = f'postgresql://{user}:{password}@{host}:{port}/{database}'        
    engine = create_engine(connection_str,  client_encoding='utf8')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    #Datenbankabfrage
    query_string = 'SELECT * FROM data_general'
    result= session.execute(text(query_string))
    
    # Ergebnis in ein JSON-Array umwandeln
    
    json_array = json.dumps([row._asdict() for row in result.fetchall()],  cls=DecimalEncoder, ensure_ascii=False).encode('utf-8')
    session.close()
    return json_array.decode('utf-8')

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
   

        

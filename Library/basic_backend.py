from sqlalchemy import create_engine,  text
from sqlalchemy.orm import sessionmaker
from decimal import Decimal
from . import query_builder as object
import json
import os

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return str(o)
        return super().default(o)

def connect_to_database():
    if os.name == 'nt':
        file = open('C:\\Users\\westp\\dexterslab\\Postgres.txt','r')
    else:
        file = open('/home/igor/dexterslab/Postgres.txt', 'r')
    database_url = file.read()
    connection_str = f'{database_url}'        
    engine = create_engine(connection_str)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def read_data(table_name):
    session = connect_to_database()
    model = object.QueryBuilder(table_name) 
    query = model.select('id', 'aspect', 'value').build()
    result= session.execute(text(query))
    json_array = json.dumps([row._asdict() for row in result.fetchall()], ensure_ascii=False).encode('utf-8')
    session.close()
    return json_array
   
    
def update_data(table_name, newAspect, newValue, id):
    try:
        session = connect_to_database()
        model = object.QueryBuilder(table_name) 
        update_query = model.set(aspect=f"{newAspect}", value = f"{newValue}").set_where(f"id = {id}").build()
        session.execute(text(update_query))
        session.commit()
    except Exception as e:
        print(e)

def insert_data(table_name, newid, newaspect, newvalue):
    try:
       session = connect_to_database()
       query_builder = object.QueryBuilder(table_name)
       data = {'id': newid, 'aspect': newaspect, 'value': newvalue}
       newaspect = f"'{newaspect}'"
       newvalue = f"'{newvalue}'"
       insert_query = query_builder.insert(id=newid, aspect=newaspect, value=newvalue).build()
       session.execute(text(insert_query), data)
       session.commit()
    except Exception as e:
        print(e)

def delete_row(id, table_name):
    try:
        session = connect_to_database()
        condition = "id = :id"
        data = {'id': id}
        query_builder = object.QueryBuilder(table_name)
        delete_query = query_builder.delete_where(condition).build()
        session.execute(text(delete_query), data)
        session.commit()
    except Exception as e:
        print(e)    



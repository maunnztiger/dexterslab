from sqlalchemy import create_engine,  text
from sqlalchemy.orm import sessionmaker
from decimal import Decimal
from . import query_builder as select_builder
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

def read_data_general():
    session = connect_to_database()
    query_builder = select_builder.QueryBuilder('data_general') 
    query = query_builder.select('general_id', 'aspect', 'value').build() 
    result= session.execute(text(query))
    json_array = json.dumps([row._asdict() for row in result.fetchall()],  cls=DecimalEncoder, ensure_ascii=False).encode('utf-8')
    session.close()
    return json_array
   
    
def update_data_general(table_name, newAsepct, newValue, id):
    try:
        session = connect_to_database()
        update_query= "UPDATE {table_name} SET aspect='{value1}', value='{value2}' WHERE general_id={value3};".format(table_name=table_name, value1=newAsepct, value2=newValue, value3=id)
        print(update_query)
        session.execute(text(update_query))
        session.commit()
    except Exception as e:
        print(e) 

def read_men_data():
    session = connect_to_database()
    query_builder = select_builder.QueryBuilder('data_men') 
    query = query_builder.select('men_id', 'aspect', 'value').build() 
    result= session.execute(text(query))
    json_array = json.dumps([row._asdict() for row in result.fetchall()],  cls=DecimalEncoder, ensure_ascii=False).encode('utf-8')
    session.close()
    return json_array

def read_special_data():
    session = connect_to_database()
    query_builder = select_builder.QueryBuilder('data_special') 
    query = query_builder.select('special_id', 'aspect', 'value').build() 
    result= session.execute(text(query))
    json_array = json.dumps([row._asdict() for row in result.fetchall()],  cls=DecimalEncoder, ensure_ascii=False).encode('utf-8')
    session.close()
    return json_array
   

        

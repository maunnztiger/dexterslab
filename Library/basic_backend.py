from sqlalchemy import create_engine,  text
from sqlalchemy.orm import sessionmaker
from decimal import Decimal
from . import query_builder as select_builder
import json

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return str(o)
        return super().default(o)

def connect_to_database():
    file = open('C:\\Users\\nn\\Documents\\Postgres.txt', 'r')
    database_url = file.read()
    connection_str = f'{database_url}'        
    engine = create_engine(connection_str)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def read_data_general():
    session = connect_to_database()
    query_builder = select_builder.QueryBuilder('data_general') 
    query = query_builder.select('id', 'aspect', 'value').build() 
    result= session.execute(text(query))
    json_array = json.dumps([row._asdict() for row in result.fetchall()], ensure_ascii=False).encode('utf-8')
    session.close()
    return json_array
   
    
def update_data(table_name, newAsepct, newValue, id):
    try:
        session = connect_to_database()
        update_query= "UPDATE {table_name} SET aspect='{value1}', value='{value2}' WHERE id={value3};".format(table_name=table_name, value1=newAsepct, value2=newValue, value3=id)
        print(update_query)
        session.execute(text(update_query))
        session.commit()
    except Exception as e:
        print(e)

def insert_data(table_name, id, aspect, value):
    try:
       session = connect_to_database()
       insert_query= "INSERT INTO {table_name} (id, aspect, value) VALUES ('{value1}','{value2}','{value3}');".format(table_name=table_name, value1=id, value2=aspect, value3=value)
       print(insert_query)
       session.execute(text(insert_query))
       session.commit()
    except Exception as e:
        print(e)

def delete_row(id, table_name):
    try:
        session = connect_to_database()
        delete_query = "DELETE FROM {table_name} WHERE id = {value};".format(table_name=table_name, value=id)
        print(delete_query)
        session.execute(text(delete_query))
        session.commit()
    except Exception as e:
        print(e)    
        

def read_men_data():
    session = connect_to_database()
    query_builder = select_builder.QueryBuilder('data_men') 
    query = query_builder.select('id', 'aspect', 'value').build() 
    result= session.execute(text(query))
    json_array = json.dumps([row._asdict() for row in result.fetchall()],  cls=DecimalEncoder, ensure_ascii=False).encode('utf-8')
    session.close()
    return json_array

def read_special_data():
    session = connect_to_database()
    query_builder = select_builder.QueryBuilder('data_special') 
    query = query_builder.select('id', 'aspect', 'value').build() 
    result= session.execute(text(query))
    json_array = json.dumps([row._asdict() for row in result.fetchall()],  cls=DecimalEncoder, ensure_ascii=False).encode('utf-8')
    session.close()
    return json_array
   

        

from sqlalchemy import create_engine,  text
from sqlalchemy.orm import sessionmaker
from decimal import Decimal
from .Querybuilder import query_builder as select
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

def read_data(table_name):
    session = connect_to_database()
    query_builder = select.QueryBuilder(table_name) 
    query = query_builder.select('id', 'aspect', 'value').build() 
    result= session.execute(text(query))
    json_array = json.dumps([row._asdict() for row in result.fetchall()], ensure_ascii=False).encode('utf-8')
    session.close()
    return json_array
   
    
def update_data(table_name, newAspect, newValue, id):
    try:
        session = connect_to_database()
        update_builder = update.UpdateQueryBuilder(table_name)        
        update_query = update_builder.set(aspect=f"{newAspect}", value = f"{newValue}").where(f"id = {id}").build()
        print(update_query)
        session.execute(text(update_query))
        session.commit()
    except Exception as e:
        print(e)

def insert_data(table_name, newid, newaspect, newvalue):
    try:
       session = connect_to_database()
       query_builder = insert.InsertQueryBuilder(table_name)
       data = {'id': newid, 'aspect': newaspect, 'value': newvalue}
       insert_query = query_builder.insert(id=newid, aspect=newaspect, value=newvalue).build()
       print(insert_query)
       session.execute(text(insert_query), data)
       session.commit()
    except Exception as e:
        print(e)

def delete_row(id, table_name):
    try:
        session = connect_to_database()
        condition = "id = :id"
        data = {'id': id}
        query_builder = delete.DeleteQueryBuilder(table_name)
        delete_query = query_builder.where(condition).build()
        print(delete_query)
        session.execute(text(delete_query), data)
        session.commit()
    except Exception as e:
        print(e)    

   

        

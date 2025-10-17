from sqlalchemy import create_engine,  text
from sqlalchemy.orm import sessionmaker
from decimal import Decimal
from werkzeug.security import generate_password_hash, check_password_hash
from . import query_builder as object
import json
import os

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return str(o)
        return super().default(o)

def connect_to_database():
 
    database_url = os.environ.get('POSTGRES_URL')
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
   
def read_data_with_index(table_name, id):
    session = connect_to_database()
    model = object.QueryBuilder(table_name)
    query = model.select('id', 'aspect', 'value').where(id=id).build()
    result = session.execute(text(query),  model.data)
    row = result.fetchone()
    session.close()

    # row ist ein SQLAlchemy Row-Objekt – in Dict umwandeln
    new_row = row._asdict() if row else None

    return new_row

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

def add_user(username, password):
    try:
        hashed_pw = generate_password_hash(password) 
        session = connect_to_database()
        print("DATA:", {'username': username, 'password_hash': hashed_pw})
        session.execute(
            text("INSERT INTO users (username, password_hash) VALUES (:username, :password_hash)"),
            {'username': username, 'password_hash': hashed_pw}
        )
        session.flush()
        session.commit()
    except Exception as e:
        print(e)    

def login_user(username):
    try:
        session = connect_to_database()
        result= session.execute(text("SELECT id, password_hash FROM users WHERE username = :username"),
        {"username": username})
        row = result.fetchone()
        session.close()
        return row
    except Exception as e:
        print(e)



def delete_row(id, table_name):
    try:
        session = connect_to_database()
        query = f"DELETE FROM {table_name} WHERE id = :id"
        session.execute(text(query), {"id": id})
        session.commit()
        session.close()
    except Exception as e:
        print(e)    



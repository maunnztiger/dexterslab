from flask import Flask, render_template, Response, request, send_from_directory, session, url_for, flash, redirect, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from Library import model as Model
import json
import os

app = Flask(__name__)
app.secret_key ="erihghrghrghgrdibgh"
app.debug = True
CORS(app, origins=["http://localhost:5000"])
json_map = {}
app.config['JSON_AS_ASCII'] = False

@app.route("/styles.css")
def styles_css():
    return render_template("styles/styles.css")

@app.route("/data.css")
def data_general_css():
    return render_template("styles/data_general.css")

@app.route("/script.js")
def script_js():
    return render_template("script.js")

@app.route("/graph.js")
def graph_js():
    return render_template("graph.js")

@app.route("/data.js")
def data_js():
    return render_template("general_data.js")

@app.route("/")
def hellou():
    if 'user_id' in session:
        return render_template("index.html")
    return render_template('login.html')
    
    

@app.route("/<string:page>")
def data_html(page):  
   return render_template(str(page))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')
 
@app.route("/data/<string:table_name>", methods=['GET'])
def get_data(table_name):
        if request.method == 'GET':
            json_array = Model.read_data(table_name)
            resp = Response(json_array , content_type='application/json; charset=utf-8')
            return resp
  
@app.route("/data/data_diagram")
def get_data_diagram():
    json_array = Model.read_data('data_european_comparation')
    data = Response(json_array , content_type='application/json; charset=utf-8')
    return data
 
@app.route("/update_row",  methods=['POST'])
def update_row():
    data = request.get_json()
    table_name = data['table_name']
    id = data['datatableIndex']  
    newAsepct = data['newAspect']
    newValue = data['newValue']
    Model.update_data(table_name, newAsepct, newValue , id)
    return json.dumps({'success':True}), 200, {'Content_type':'application/json; charset=utf-8'}
    
@app.route("/insert_row", methods=['POST'])
def insert_row():
    data = request.get_json()
    table_name = data["table_name"]
    newid = data["index"]
    newaspect = data['aspect']
    newvalue = data["value"]
    print(f"insert_row: table={table_name}, id={newid}, aspect={newaspect}, value={newvalue}", flush=True)

    Model.insert_data(table_name, newid, newaspect, newvalue)
    new_row = Model.read_data_with_index(table_name, newid)   
    return jsonify({'success':True, 'new_row': new_row}), 200

@app.route("/delete_row", methods=['POST'])
def delete_row():
    data = request.get_json()
    id = data['id']
    table_name = data['table_name']
    print(id, table_name)
    Model.delete_row(id, table_name)
    return json.dumps({'success':True}), 200, {'Content_type':'application/json; charset=utf-8'}

@app.route("/add_new_user", methods=['POST'])
def add_user():
    data = request.get_json()
    username = data["username"]
    password = data['password']
    print(username, password)
    Model.add_new_user(username, password) 
    return json.dumps({'success':True}), 200, {'Content_type':'application/json; charset=utf-8'}


@app.route("/login", methods=['POST'])
def login():
    username = request.form['uname']
    password = request.form['psw']
    result = Model.login(username)
    if result:
        user_id, password_hash = result
        if check_password_hash(password_hash, password):
            session['user_id'] = user_id
            session['username'] = username
            return render_template('index.html', username=username)
        else:
            flash('Falsches Passwort')
            return render_template('login.html')
    else:
        flash('Benutzer nicht gefunden')
   
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Session löschen
    session.clear()
    # Zurück zur Login-Seite
    return render_template('login.html')  
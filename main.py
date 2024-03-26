from flask import Flask, render_template, Response, request, send_from_directory
from Library import model as Model
import json
import os

app = Flask(__name__)

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
    return render_template("index.html")

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
    print(newid, newaspect, newvalue)
    Model.insert_data(table_name, newid, newaspect, newvalue)
    return json.dumps({'success':True}), 200, {'Content_type':'application/json; charset=utf-8'}

@app.route("/delete_row", methods=['POST'])
def delete_row():
    data = request.get_json()
    id = data['id']
    table_name = data['table_name']
    print(id, table_name)
    Model.delete_row(id, table_name)
    return json.dumps({'success':True}), 200, {'Content_type':'application/json; charset=utf-8'}

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
     
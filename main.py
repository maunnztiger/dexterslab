from flask import Flask, render_template, Response, request, redirect, session, jsonify
from Library import model as Model
import json


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/styles.css")
def styles_css():
    return render_template("styles/styles.css")

@app.route("/data_general.css")
def data_general_css():
    return render_template("styles/data_general.css")



@app.route("/script.js")
def script_js():
    return render_template("script.js")

@app.route("/general_data.js")
def general_data_js():
    return render_template("general_data.js")

@app.route("/")
def hellou():
    return render_template("index.html")

@app.route("/general_data_html")
def get_general_data_html():  
   return render_template("general_data.html")

    
@app.route("/men_data_html")
def get_men_data_html():
    return render_template("men_data.html")

@app.route("/general_data")
def get_general_data():
    json_array = Model.read_data_general()
    data = Response(json_array , content_type='application/json; charset=utf-8')
    return data

@app.route("/men_data")
def get_men_data():
    json_array = Model.read_men_data()
    data = Response(json_array, content_type='application/json; charset=utf-8')
    return data

@app.route("/data_special_html")
def get_data_special_html():
    return render_template("data_special.html")

@app.route("/data_special")
def get_special_data():
    json_array = Model.read_special_data()
    data = Response(json_array, content_type='application/json; charset=utf-8')
    return data

@app.route("/general_data_update_row",  methods=['POST'])
def general_data_update_row():
    data = request.get_json()
    id = data['datatableIndex']
    newAsepct = data['newAspect']
    newValue = data['newValue']
    Model.update_data_general('data_general',newAsepct, newValue , id)
    return json.dumps({'success':True}), 200, {'Content_type':'application/json; charset=utf-8'}
    

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
     
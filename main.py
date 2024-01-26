from flask import Flask, render_template, Response
from Library import model
#import os
from sqlalchemy import create_engine




app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def hellou():
    return render_template("index.html")


@app.route("/script.js")
def script_js():
    return render_template("script.js")


@app.route("/styles.css")
def styles_css():
    return render_template("styles/styles.css")

@app.route("/general_data.js")
def general_data_js():
    return render_template("general_data.js")


@app.route("/general_data")
def get_general_data():
    json_array = model.read_items()
    data = Response(json_array , content_type='application/json; charset=utf-8')
    return data

@app.route("/general_data_html")
def get_general_data_html():  
   return render_template("general_data.html")
   
if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
     
from flask import Flask, render_template, send_from_directory
from Library import basic_backend
#import os
from sqlalchemy import create_engine




app = Flask(__name__)


@app.route("/")
def hellou():
    return render_template("index.html")


@app.route("/script.js")
def javascript():
    return render_template("script.js")


@app.route("/getData")
def get_data():
    json_array = basic_backend.read_items()
    return json_array 
   
   
if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
     
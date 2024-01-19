from flask import Flask, render_template, Response
from Library import basic_backend
#import os
from sqlalchemy import create_engine




app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def hellou():
    return render_template("index.html")


@app.route("/script.js")
def javascript():
    return render_template("script.js")


@app.route("/getData")
def get_data():
    json_array = basic_backend.read_items()
    # print(json_array)
    response= Response(json_array , content_type='application/json; charset=utf-8')
    return response
   
   
if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
     
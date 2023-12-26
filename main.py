from flask import Flask, render_template, send_from_directory
from Library import data as dataframe
import os


app = Flask(__name__)


@app.route("/")
def hellou():
    
    # dataframe.df.to_json("products.json", orient="records",lines=True, mode="w")
    return render_template("index.html")


@app.route("/script.js")
def javascript():
    return render_template("script.js")


@app.route("/getData")
def get_data():
    
    with open("products.json", 'r') as myfile:
        data = myfile.read()
    return data    


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
    

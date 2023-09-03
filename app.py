from chandata import chancountry
from comb import combfunc
from subRed import reddit
from rawvssports import dailysports

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/chanData", methods = ["GET","POST"])
def fourchanDatahtml():
    value = request.form.get("country")
    final = chancountry(value)
    return render_template(final+".html")

@app.route("/comb", methods=["GET","POST"])
def combinedData():
    combfunc()
    return render_template("comb.html")

@app.route("/subred", methods=["GET","POST"])
def subreddData():
    reddit()
    return render_template("subred.html")

@app.route("/rawsports", methods=["GET","POST"])
def sportsraw():
    dailysports()
    return render_template("dailysports.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
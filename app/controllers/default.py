from flask import render_template
from app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/account/<user>")
@app.route("/account/", defaults={'user':None})
def acoount(user):
    return render_template('account.html', user=user)
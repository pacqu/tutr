import jinja2
from flask import Flask
from flask import redirect, render_template, request, session, url_for

from db import DatabaseManager
from util import Util

app = Flask(__name__)
dbm = DatabaseManager.create()


@app.route('/', methods=["GET","POST"])
def home():
    if request.method == "POST":
        sub = request.form['submit']
        if sub == "register":
            return redirect(url_for('register'))
        elif sub == "login":
            return redirect(url_for('login'))
    else:
        return render_template("index.html")

@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == "POST":
        = request.form['']
    else:
        return render_template("register.html")

@app.route('/login', methods=["GET","POST"])  
def login():
  return render_template("index.html")

if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0',port=8000)

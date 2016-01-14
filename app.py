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
        fullname = request.form['fullname']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['confirmPassword']
        #bioline = request.form['bioline']
        bioline = "testing fam"
        if  password == cpassword:
            if dbm.register_user(email, fullname, password, bioline):
                return str(dbm.fetch_all_users())
            else:
                return render_template("register.html", message = "email already used")
        else:
            return render_template("register.html",message = "passwords do not match")
    else:
        return render_template("register.html")

@app.route('/login', methods=["GET","POST"])  
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        if dbm.is_user_authorized(email,password):
            return "login worked!"
        else:
            return render_template("login.html", message = "Email/Password Incorrect")
    else:
      return render_template("login.html")
    
if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0',port=8000)

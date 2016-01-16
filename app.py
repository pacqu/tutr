import jinja2
from flask import Flask
from flask import redirect, render_template, request, session, url_for

from db import DatabaseManager
from util import Util

app = Flask(__name__)
app.secret_key = 'jgjb3st'

dbm = DatabaseManager.create()


@app.route('/', methods=["GET","POST"])
def home():
    if session.get('user', None):
        return redirect('/dashboard')
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
    if session.get('user', None):
        return redirect('/dashboard')
    if request.method == "POST":
        fullname = request.form['fullname']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['confirmPassword']
        bioline = request.form['bioline']
        #bioline = "testing fam"
        if  password == cpassword:
            if dbm.register_user(email, fullname, password, bioline):
                session['user']=email
                #return str(dbm.fetch_all_users())
                return redirect('/dashboard')
            else:
                return render_template("register.html", message = "email already used")
        else:
            return render_template("register.html",message = "passwords do not match")
    else:
        return render_template("register.html")

@app.route('/login', methods=["GET","POST"])  
def login(message ="login to tut.r"):
    if session.get('user', None):
        return redirect('/dashboard')
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        if dbm.is_user_authorized(email,password):
            session['user'] = email
            return redirect(url_for('dashboard'))
        else:
            return render_template("login.html", message = "Email/Password Incorrect")
    else:
      return render_template("login.html", message = message)


@app.route('/dashboard', methods=["GET","POST"])
def dashboard():
    if session.get('user', None):
        if request.method == "POST":
            page = request.form['page']
            if page == "Find a Tutor":
                return render_template()
            elif page == "Register as a Tutor":
                return render_template()
            elif page == "Edit Account Info":
                return redirect(url_for('settings'))
            elif page == "Log Off":
                return redirect(url_for('logoff'))
            else:
                return render_template("dashboard.html", 
                                       user = dbm.get_name(session.get('user',None)))
        else:
            return render_template("dashboard.html", 
                                   user = dbm.get_name(session.get('user',None)))
    else:
        return login(message="you must log in to access dashboard")
        
@app.route('/logoff')
def logoff():
    if session.get('user', None):
        session['user'] = 0
    return redirect('/')

@app.route('/settings', methods=["GET","POST"])
def settings(message="want to update your info, fam?"):
    user = session.get('user', None)
    if user:
        if request.method == "POST":
            newname = request.form['editname']
            newbio = request.form['editbio']
            newlocation = request.form['editlocation']
            oldpassword = request.form['oldpassword']
            newpassword = request.form['newpassword']
            confirmpassword = request.form['confirmpassword']
            if oldpassword == "":
                dbm.edit_user(user, newname, newbio, newlocation)
                return render_template("settings.html",
                                       name = dbm.get_name(session.get('user',None)), 
                                       bioline = dbm.get_bio(session.get('user',None)), 
                                       location = dbm.get_location(session.get('user',None)), 
                                       message = "info updated successfully"
                                       )
        else:
            print dbm.get_name(session.get('user',None)) 
            return render_template("settings.html",
                                   name = dbm.get_name(session.get('user',None)), 
                                   bioline = dbm.get_bio(session.get('user',None)), 
                                   location = dbm.get_location(session.get('user',None)), 
                                   message = message
                                   )
    else:
        return login(message="you must log in to access dashboard")
        

if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0',port=8000)

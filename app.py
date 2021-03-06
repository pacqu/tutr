import jinja2, json
from flask import Flask
from flask import redirect, render_template, request, session, url_for

from db import DatabaseManager
from util import Util

add_hard_code = 0

application = Flask(__name__)
application.secret_key = 'jgjb3st'

dbm = DatabaseManager.create()

change = dbm.register_user("tutr@tutr.com","Jess Tutr","pass","Expert at Bio")
if change == True:
    dbm.change_availability("tutr@tutr.com")
dbm.register_user("tutee","da tutee","pass","hardcoded tutee for testing")
    
print dbm.fetch_all_users()

@application.route('/', methods=["GET","POST"])
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

@application.route('/register', methods=["GET","POST"])
def register():
    if session.get('user', None):
        return redirect('/dashboard')
    if request.method == "POST":
        fullname = request.form['fullname']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['confirmPassword']
        bioline = request.form['bioline']
        if  password == cpassword:
            if dbm.register_user(email, fullname, password, bioline):
                session['user']=email
                return redirect('/dashboard')
            else:
                return render_template("register.html", message = "email already used")
        else:
            return render_template("register.html",message = "passwords do not match")
    else:
        return render_template("register.html")

@application.route('/login', methods=["GET","POST"])  
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


@application.route('/dashboard', methods=["GET","POST"])
def dashboard():
    user = session.get('user', None)
    if user:
        #print dbm.fetch_all_users()
        if dbm.is_user_available(user) == True:
            dbm.change_availability(user)
        if dbm.is_user_match(user) == True:
            dbm.change_match(user)
        dbm.add_matched_user(user, 'none')
        if request.method == "POST":
            page = request.form['page']
            if page == "find a tut.r":
                return redirect(url_for('regastutee'))
            elif page == "register as a tut.r":
                return redirect(url_for('regastutr'))
            elif page == "edit account info":
                return redirect(url_for('settings'))
            elif page == "log off":
                return redirect(url_for('logoff'))
            else:
                ut = session.get('user', None)
                return render_template("dashboard.html", 
                                       user = dbm.get_name(session.get('user',None)))
        else:
            return render_template("dashboard.html", 
                                   user = dbm.get_name(session.get('user',None)))
    else:
        return login(message="you must log in to access dashboard")
@application.route('/logoff')
def logoff():
    if session.get('user', None):
        session['user'] = 0
    return redirect('/')

@application.route('/settings', methods=["GET","POST"])
def settings():
    user = session.get('user', None)
    if user:
        if request.method == "POST":
            page = request.form['submit']
            if page == "save changes":
                newname = request.form['editname']
                newbio = request.form['editbio']
                newlocation = request.form['editlocation']
                dbm.edit_user(user, newname, newbio, newlocation)
                return render_template("settings.html",
                                       name = dbm.get_name(session.get('user',None)), 
                                       bioline = dbm.get_bio(session.get('user',None)), 
                                       location = dbm.get_location(session.get('user',None)), 
                                       message = "info updated successfully")
            else:
                return redirect(url_for('dashboard'))
        else:
            return render_template("settings.html",
                                   name = dbm.get_name(session.get('user',None)), 
                                   bioline = dbm.get_bio(session.get('user',None)), 
                                   location = dbm.get_location(session.get('user',None)), 
                                   message = "want to update your info, fam?"
                                   )
    else:
        return login(message="you must log in to access dashboard")
        
@application.route('/regastutr', methods=["GET","POST"])
def regastutr():
    user = session.get('user', None)
    if user:
        if request.method == "POST":
            page = request.form['page']
            if page == "tut.r me up, fam":
                if dbm.change_availability(user):
                    return redirect(url_for('posttutr'))
                else:
                    return redirect(url_for('dashboard'))
            else:
                return redirect(url_for('dashboard'))
        else:
            return render_template("regat.html", 
                                   user = dbm.get_name(session.get('user',None)) )
    else:
        return login(message="you must log in to access tut.r registration")

@application.route('/posttutr', methods=["GET","POST"])
def posttutr():
    user = session.get('user', None)
    if user:
        if request.method == 'POST':
            dbm.change_match(user)
            dbm.add_matched_user(user, 'none')
            return redirect(url_for('dashboard'))
        else:
            return render_template('posttutr.html')
    else:
        return login(message="you must log in to access tut.r registration")

@application.route('/setmatch', methods = ['GET'])
def setmatch():
    user = session.get('user', None)
    dbm.change_match(user)
    dbm.change_availability(user)
    dbm.add_matched_user(user, 'tutee')
    return dbm.get_matched_user(user) + ' matched with tutr!'

@application.route('/getstatus', methods = ['GET'])
def getstatus():
    user = session.get('user', None)
    matched_user = {'tuteeName':'no user',
                    'tuteeEmail':'no email',
                    'tuteeLocation':'no loction',
                    'tuteeBio':'no bio',
                    'status':'looking for the perfect tutee'}
    #print dbm.get_user(user)
    #print dbm.is_user_match(user)
    if dbm.is_user_match(user) == True:
        tutee = dbm.get_matched_user(user)
        matched_user['tuteeName'] = dbm.get_name(tutee)
        matched_user['tuteeEmail'] = tutee
        matched_user['tuteeLocation'] = dbm.get_location(tutee)
        matched_user['tuteeBio'] = dbm.get_bio(tutee)
        matched_user['status'] = "found the perfect tutee! return to dashboard when you're finished!"
    #print matched_user
    return json.JSONEncoder().encode(matched_user)
        
@application.route('/regastutee', methods=["GET","POST"])
def regastutee():
    user = session.get('user', None)
    if user:
        if request.method == "POST":
            page = request.form['page']
            if page == "tutee me up, fam":
                return redirect(url_for('posttutee'))
            else:
                return redirect(url_for('dashboard'))
        else:
            return render_template("regtutee.html",
                                   user = dbm.get_name(session.get('user',None)) )
    else:
        return login(message="you must log in to access tut.r registration")

@application.route('/postutee', methods=["GET","POST"])
def posttutee():
    user = session.get('user', None)
    if user:
        if request.method == 'POST':
            return redirect(url_for('dashboard'))
        else:
            return render_template('posttutee.html',
                                   user = dbm.get_name(session.get('user',None)) )
    else:
        return login(message="you must log in to access tutee registration")

@application.route('/gettutrlist',methods=["GET"])
def gettutrlist():
    availusers = dbm.get_available_users()
    #print availusers
    return json.JSONEncoder().encode(availusers)

@application.route('/gettutr/<tutr>', methods=["GET"])
def gettutr(tutr=''):
    '''What This Should Do:
    - Takes Tutr's Username (Email)
    - Sets Tutee & Tutr's Matched/Macthed Users Fields
    - Makes Tutr unavailable
    - Sends JSON containing Tutr's info
    '''
    user = session.get('user', None)
    sendtutr = dbm.get_user(tutr)
    #set tutr/tutee as each other's matched users
    dbm.add_matched_user(user,tutr)
    dbm.add_matched_user(tutr,user)
    #change tutr availability
    #print dbm.get_user(tutr)
    #print dbm.is_user_available(tutr)
    dbm.change_match(tutr)
    dbm.change_availability(tutr)
    #print dbm.is_user_available(tutr)
    matched_tutr = {'tutrName': dbm.get_name(tutr),
                    'tutrEmail': tutr,
                    'tutrLocation':dbm.get_location(tutr),
                    'tutrBio': dbm.get_bio(tutr),
                    'tutrAvail': dbm.get_user(tutr)[4]}
    return json.JSONEncoder().encode(matched_tutr)

@application.route('/getallusers', methods=["GET"])
def getallusers():
    users = dbm.fetch_all_users()
    return json.JSONEncoder().encode(users)

if __name__ == '__main__':
    application.debug = True
    application.run(host='0.0.0.0')
    

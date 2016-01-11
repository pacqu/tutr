import jinja2
from flask import Flask
from flask import redirect, render_template, request, session

from db import DatabaseManager
from util import Util

app = Flask(__name__)
dbm = DatabaseManager.create()


@app.route('/')
@app.route('/home')
def home():
  return render_template('index.html')

if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0',port=8000)

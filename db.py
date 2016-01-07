# Code based on bloginator database manager authored by Alvin Lin (alvin.lin@stuypulse.com)
import sqlite3
import time

from util import Util

DATABASE = 'database/tutr.db'

class DatabaseManager():
  def __init__(self, database):
    self.database = database

  @staticmethod
  def create():
    connection = sqlite3.connect(DATABASE);
    c = connection.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
              fullname text NOT NULL PRIMARY KEY,
              password text NOT NULL,
              bioline text NOT NULL,
              availability text NOT NULL,
              match text NOT NULL,
              location text NOT NULL);
              """)
    connection.commit()
    connection.close()
    return DatabaseManager(DATABASE)
  
  #methods needed:
  #register user 
   def register_user(self, fullname, password, password, bioline):
    connection = sqlite3.connect(self.database);
    c = connection.cursor()
    result = True
    try:
      c.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)',
                (fullname, Util.hash(password), bioline, 'unavailable', 'unmatched','unknown' ))
    except sqlite3.IntegrityError:
      result = False
    connection.commit()
    connection.close()
    return result

 
  def is_user_authorized(self, fullname, password):
    connection = sqlite3.connect(self.database)
    c = connection.cursor()
    # We can assume username is a unique field.
    c.execute('SELECT password FROM users WHERE username=?',
              (fullname,))
    actual_password = c.fetchone()
    connection.close()
    if actual_password:
      return actual_password[0] == Util.hash(password)
    return False

  #change user info
  def edit_user(self, user_id, fullname, password, bioline, location):
    connection = sqlite3.connect(self.database)
    c = connection.cursor()
    try:
      c.execute("""
                UPDATE users SET fullname=?,password=?,bioline=?,location=?
                WHERE rowid=?
                """,
                (fullname, password, bioline, location, user_id))
      connection.commit()
      connection.close()
      return True
    except:
      connection.close()
  return False

  #change availability
  def is_user_available(self, user_id):
    connection = sqlite3.connect(self.database)
    c = connection.cursor()
    # We can assume username is a unique field.                                                                                                                                      
    c.execute('SELECT availability FROM users WHERE rowid=?',
              (user_id,))
    avail = c.fetchone()
    connection.close()
    if avail == 'available':
      return True
    return False
    
  def change_availability(self, user_id):
    if is_user_available:
      avail = 'unavailable'
    else:
      avail = 'available'
      connection = sqlite3.connect(self.database)
      c = connection.cursor()
      try:
        c.execute("""                                                                                                                                                                  
                UPDATE users SET availability=?                                                                                                          
                WHERE rowid=?                                                                                                                                                        
                """,
                  (avail, user_id))
        connection.commit()
        connection.close()
      return True
    except:
      connection.close()
    return False

  #change matched
  def is_user_match(self, user_id):
    connection = sqlite3.connect(self.database)
    c = connection.cursor()
    c.execute('SELECT match FROM users WHERE rowid=?',
              (user_id,))
    mat = c.fetchone()
    connection.close()
    if mat == 'matched':
      return True
    return False

  def change_match(self, user_id):
    if is_user_match:
      mat ='unmatched'
    else:
      mat ='matched'
  connection = sqlite3.connect(self.database)
  c = connection.cursor()
  try:
    c.execute("""
                UPDATE users SET match=?                                                                                                                           
                WHERE rowid=?
                """,
              (mat, user_id))
    connection.commit()
    connection.close()
    return True
  except:
    connection.close()
    return False

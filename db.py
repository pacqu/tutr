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
              username text NOT NULL PRIMARY KEY,
              fullname text NOT NULL,
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
  def register_user(self, username, fullname, password, bioline):
    connection = sqlite3.connect(self.database);
    c = connection.cursor()
    result = True
    try:
      c.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)',
                (username, fullname, Util.hash(password), bioline, 'unavailable', 'unmatched','unknown' ))
    except sqlite3.IntegrityError:
      result = False
    connection.commit()
    connection.close()
    return result

 
  def is_user_authorized(self, username, password):
    connection = sqlite3.connect(self.database)
    c = connection.cursor()
    # We can assume username is a unique field.
    c.execute('SELECT password FROM users WHERE username=?',
              (username,))
    actual_password = c.fetchone()
    connection.close()
    if actual_password:
      return actual_password[0] == Util.hash(password)
    return False

  #change user info
  def edit_user(self, username, fullname, password, bioline, location):
    connection = sqlite3.connect(self.database)
    c = connection.cursor()
    try:
      c.execute("""
                UPDATE users SET fullname=?,password=?,bioline=?,location=?
                WHERE rowid=?
                """,
                (fullname, password, bioline, location, username))
      connection.commit()
      connection.close()
      return True
    except:
      connection.close()
      return False

  #change availability
  def is_user_available(self, username):
    connection = sqlite3.connect(self.database)
    c = connection.cursor()
    # We can assume username is a unique field.                                                                                                                                      
    c.execute('SELECT availability FROM users WHERE username=?',
              (username,))
    avail = c.fetchone()
    connection.close()
    if avail == 'available':
      return True
    return False
    
  def change_availability(self, username):
    if self.is_user_available:
      avail = 'unavailable'
    else:
      avail = 'available'
    connection = sqlite3.connect(self.database)
    c = connection.cursor()
    try:
      c.execute("""                                                                                                                                                                  
                UPDATE users SET availability=?                                                                                                          
                WHERE username=?                                                                                                                                                        
                """,
                (avail, username))
      connection.commit()
      connection.close()
      return True
    except:
      connection.close()
      return False

  #change matched
  def is_user_match(self, username):
    connection = sqlite3.connect(self.database)
    c = connection.cursor()
    c.execute('SELECT match FROM users WHERE username=?',
              (username,))
    mat = c.fetchone()
    connection.close()
    if mat == 'matched':
      return True
    return False

  def change_match(self, username):
    if self.is_user_match:
      mat ='unmatched'
    else:
      mat ='matched'
    connection = sqlite3.connect(self.database)
    c = connection.cursor()
    try:
      c.execute("""
                UPDATE users SET match=?                                                                                                                           
                WHERE username=?
                """,
                (mat, username))
      connection.commit()
      connection.close()
      return True
    except:
      connection.close()
      return False

  def fetch_all_users(self):
    connection = sqlite3.connect(self.database)
    c = connection.cursor()
    c.execute('SELECT * FROM users');
    users = c.fetchall()
    connection.close()
    return users

if __name__== '__main__':
  d = DatabaseManager.create()
  d.register_user("test","marty marty" , 'password', 'ayylmao')
  users = d.fetch_all_users()
  test = users[0]
  print test
  print 'Should Be False'
  print d.is_user_available(test[0]);
  print d.change_availability(test[0]);
  users1 = d.fetch_all_users()
  test1 = users1[0]
  print test1

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
              email text NOT NULL PRIMARY KEY,
              fullname text NOT NULL,
              password text NOT NULL,
              bioline text NOT NULL,
              availability text NOT NULL,
              match text NOT NULL,
              location text NOT NULL,
              matcheduser text NOT NULL);
              """)
    connection.commit()
    connection.close()
    return DatabaseManager(DATABASE)
  

  #methods needed:
  #register user 
  def register_user(self, email, fullname, password, bioline):
    connection = sqlite3.connect(self.database);
    c = connection.cursor()
    result = True
    try:
      c.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                (email, fullname, Util.hash(password), bioline, 'unavailable', 'unmatched','unknown location','none' ))
    except sqlite3.IntegrityError:
      result = False
    connection.commit()
    connection.close()
    return result
  
  def is_user_authorized(self, email, password):
    connection = sqlite3.connect(self.database)
    c = connection.cursor()
    # We can assume username is a unique field.
    c.execute('SELECT password FROM users WHERE email=?',
              (email,))
    actual_password = c.fetchone()
    connection.close()
    if actual_password:
      return actual_password[0] == Util.hash(password)
    return False

  #change user info
  def edit_user(self, email,fullname, bioline, location):
    connection = sqlite3.connect(self.database)
    c = connection.cursor()
    try:
      c.execute("""
                UPDATE users SET fullname=?,bioline=?,location=?
                WHERE email=?
                """,
                (fullname, bioline, location, email))
      connection.commit()
      connection.close()
      return True
    except:
      connection.close()
      return False

  #get user using email  
  def get_user(self, email):
    connection = sqlite3.connect(self.database)
    c = connection.cursor()
    c.execute('SELECT * FROM users WHERE email=?',
              (email,));
    user = c.fetchone()
    connection.close()
    return user
  
  #methods to get user info using email
  def get_name(self,email):
    return self.get_user(email)[1]
  
  def get_bio(self,email):
    return self.get_user(email)[3]

  def get_location(self,email):
    return self.get_user(email)[6]

  def get_pass(self,email):
    return self.get_user(email)[2]
  
  def get_matched_user(self,email):
   return self.get_user(email)[7]

  #change availability
  def is_user_available(self, email):
    connection = sqlite3.connect(self.database)
    c = connection.cursor()
    # We can assume username is a unique field.                                                                                                                                      
    c.execute('SELECT availability FROM users WHERE email=?',
              (email,))
    avail = c.fetchone()[0]
    connection.close()
    if avail == 'available':
      return True
    return False
    
  def change_availability(self, email):
    if self.is_user_available(email) == True:
      avail = 'unavailable'
    else:
      avail = 'available'
    connection = sqlite3.connect(self.database)
    c = connection.cursor()
    try:
      c.execute("""                                                                                                                                                                  
                UPDATE users SET availability=?                                                                                                          
                WHERE email=?                                                                                                                                                        
                """,
                (avail, email))
      connection.commit()
      connection.close()
      return True
    except:
      connection.close()
      return False

  #change matched
  def is_user_match(self, email):
    connection = sqlite3.connect(self.database)
    c = connection.cursor()
    c.execute('SELECT match FROM users WHERE email=?',
              (email,))
    mat = c.fetchone()[0]
    connection.close()
    #print 'this is the match var: ' + mat[0]
    if mat == 'matched':
      return True
    return False

  def change_match(self, email):
    if self.is_user_match(email) == True:
      mat ='unmatched'
    else:
      mat ='matched'
    connection = sqlite3.connect(self.database)
    c = connection.cursor()
    try:
      c.execute("""
                UPDATE users SET match=?                                                                                                                           
                WHERE email=?
                """,
                (mat, email))
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

  def add_matched_user(self, email, matcheduser):
    connection = sqlite3.connect(self.database)
    c = connection.cursor()
    try:
      c.execute("""                                                                                                                                                                 
                UPDATE users SET matcheduser=?
                WHERE email=?
                """,
                (matcheduser, email))
      connection.commit()
      connection.close()
      return True
    except:
      connection.close()
      return False
    
  def get_available_users(self):
    allusers = self.fetch_all_users()
    availusers = []
    for user in allusers:
      if user[4] == 'available':
        availusers.append(user)
    return availusers
    
if __name__== '__main__':
  d = DatabaseManager.create()
  d.register_user("test1","marky marky" , 'password', 'ayylmao')
  users = d.fetch_all_users()
  test = users[0]
  print test
  print 'Should Be False'
  print d.is_user_available(test[0]);
  print d.change_availability(test[0]);
  users1 = d.fetch_all_users()
  test1 = users1[0]
  print test1
  print 'next shoud be same'
  print d.get_user("test1")
  print 'name: ' + d.get_name("test1")
  print 'pass: ' + d.get_pass("test1")
  print 'bio: ' + d.get_bio("test1")
  print 'location: ' + d.get_location("test1")
  print 'matched user: ' + d.get_matched_user("test1")
  print d.add_matched_user("test1", "matched user added")
  users1 = d.fetch_all_users()
  test1 = users1[0]
  print test1
  print 'matched user: ' + d.get_matched_user("test1")
  print 'should list available dude'
  print d.get_available_users()

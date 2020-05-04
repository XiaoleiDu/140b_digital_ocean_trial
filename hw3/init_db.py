# Import MySQL Connector Driver
import mysql.connector as mysql

# Load the credentials from the secured .env file
import os
import datetime
from dotenv import load_dotenv
load_dotenv('credentials.env')

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST']

print(db_user)
print(db_pass)
print(db_name)
print(db_host)

# Connect to the database
db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
cursor = db.cursor()

# # CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!!
cursor.execute("drop table if exists TStudents;")
cursor.execute("drop table if exists Tcuser;")
cursor.execute("drop table if exists Moves;")

# Create a TUsers table (wrapping it in a try-except is good practice)
cursor.execute("""
    CREATE TABLE TUsers (
      id integer  AUTO_INCREMENT PRIMARY KEY,
      firstname      VARCHAR(30) NOT NULL,
      lastname         VARCHAR(30) NOT NULL,
      email       VARCHAR(30) NOT NULL,
      created_at  TIMESTAMP
    );
""")

  
# Create a Moves table (wrapping it in a try-except is good practice)
# try:
  # cursor.execute("""
    # CREATE TABLE Moves (
      # moveId integer  AUTO_INCREMENT PRIMARY KEY,
      # jetbotId       VARCHAR(30) NOT NULL,
      # initialTime TIMESTAMP;
      # startTime TIMESTAMP;
      # endTime TIMESTAMP;
      # direction      VARCHAR(30) NOT NULL,
      # userId         VARCHAR(30) NOT NULL,
      # status       VARCHAR(30) NOT NULL
    # );
  # """)
# except:
  # print("Table already exists. Not recreating it.")

# Create a TStudents table (wrapping it in a try-except is good practice)
# try:
  # cursor.execute("""
    # CREATE TABLE Tcuser (
      # id integer  AUTO_INCREMENT PRIMARY KEY,
      # userid      VARCHAR(30) NOT NULL,
      # pwd         VARCHAR(30) NOT NULL,
      # status       VARCHAR(30) NOT NULL,
      # created_at  TIMESTAMP
    # );
  # """)
# except:
  # print("Table already exists. Not recreating it.")


# Selecting Records
cursor.execute("select * from TUsers;")
print('---------- DATABASE INITIALIZED ----------')
[print(x) for x in cursor]

db.close()
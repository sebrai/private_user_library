from flask import Flask, render_template, request
import mysql.connector
from dotenv import load_dotenv
import sys
import os
load_dotenv()
password = os.getenv("password")
host = os.getenv("host")
port = os.getenv("port")
userdb = os.getenv("user")
dbname = os.getenv("db")
app =Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/members')
def members():
    mydb = mysql.connector.connect(
    host = host,
    port= int(port),
    user = userdb,
    password = password, 
    database = dbname,
    use_pure=True
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM members")
    result = mycursor.fetchall()
    print(result)
    return render_template('members.html',data =result)

@app.route('/events')
def events():
    return render_template('upcomming.html')


@app.route('/acomplishments')
def done():
    return  render_template('done.html')

if __name__ == '__main__':
    app.run(debug =True)
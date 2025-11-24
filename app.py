from flask import Flask, render_template, request
import mysql.connector
from dotenv import load_dotenv
import sys
import os
load_dotenv()
password = os.getenv("password")
app =Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/members')
def members():
    mydb = mysql.connector.connect(
    host = "10.200.14.13",
    port= 3306,
    user = 'evillm',
    password = password, 
    database = 'evil_lm',
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
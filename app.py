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
    fresult = []
    for items in result:
       thing = (items[0],items[1],items[2],items[3].isoformat())
       fresult.append(thing)
    # print(result,format_result)
    return render_template('members.html',data = fresult)

@app.route('/members/alter/<id>', methods=['GET','POST'])
def alter(id):
    if request.method == 'POST':
        name = request.form['name']
        email =request.form['email']
        mydb = mysql.connector.connect(
            host = host,
            port= int(port),
            user = userdb,
            password = password, 
            database = dbname,
            use_pure=True
        )
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE members SET name = %s , email = %s WHERE id = %s",(name,email,id))
        mydb.commit()
        mycursor.execute("SELECT * FROM members")
        result = mycursor.fetchall()
        fresult = []
        for items in result:
            thing = (items[0],items[1],items[2],items[3].isoformat())
            fresult.append(thing)
        return render_template('members.html',data = fresult)
    else:
        mydb = mysql.connector.connect(
             host = host,
            port= int(port),
            user = userdb,
            password = password, 
            database = dbname,
            use_pure=True
            )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT name,email FROM members WHERE id = %s", (id,))
        result = mycursor.fetchall()
        name = "this is not a part of db"
        if result:
            name = result[0][0]
        return render_template('altermem.html', data = result,memname = name)


@app.route('/members/delete/<id>')
def delete(id):
    mydb = mysql.connector.connect(
    host = host,
    port= int(port),
    user = userdb,
    password = password, 
    database = dbname,
    use_pure=True
    )
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM members WHERE id = %s",(id,))
    #this remains uncommit ass i dont have a way to add back members that are deleted





    mycursor.execute("SELECT * FROM members")
    result = mycursor.fetchall()
    fresult = []
    for items in result:
       thing = (items[0],items[1],items[2],items[3].isoformat())
       fresult.append(thing)
    return render_template('members.html',data = fresult)

@app.route('/members/add')
def addmem():
    return "yay you want to add a member"

@app.route('/events')
def events():
    return render_template('upcomming.html')


@app.route('/acomplishments')
def done():
    return  render_template('done.html')

if __name__ == '__main__':
    app.run(debug =True)
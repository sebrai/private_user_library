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

@app.route('/members') # all pages dedaceded to the members page ------------------------------------------------------------------------------------
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
    mydb.commit()





    mycursor.execute("SELECT * FROM members")
    result = mycursor.fetchall()
    fresult = []
    for items in result:
       thing = (items[0],items[1],items[2],items[3].isoformat())
       fresult.append(thing)
    return render_template('members.html',data = fresult)

@app.route('/members/add', methods=['GET','POST'])
def addmem():
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
        mycursor.execute("INSERT INTO members (name,email) VALUES(%s,%s)",(name,email))
        mydb.commit()
        mycursor.execute("SELECT * FROM members")
        result = mycursor.fetchall()
        fresult = []
        for items in result:
            thing = (items[0],items[1],items[2],items[3].isoformat())
            fresult.append(thing)
        return render_template('members.html',data = fresult)
    else:
        return render_template('addmem.html')
@app.route('/events')  # all pages dedaceded to the events page ------------------------------------------------------------------------------------
def events():
    mydb = mysql.connector.connect(
    host = host,
    port= int(port),
    user = userdb,
    password = password, 
    database = dbname,
    use_pure=True
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM events WHERE done = 0")
    result = mycursor.fetchall()
    return render_template('upcomming.html', data = result)

@app.route('/events/finish/<id>')
def finish(id):
    mydb = mysql.connector.connect(
    host = host,
    port= int(port),
    user = userdb,
    password = password, 
    database = dbname,
    use_pure=True
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM events WHERE id = %s",(id,))
    updateitem = mycursor.fetchone()
    print(updateitem[5],type(updateitem[5]),"whole:",updateitem)
    if updateitem[5] == 0 :
        mycursor.execute("INSERT INTO done(title,descr,event_id) VALUES(%s,%s,%s)",(updateitem[1],updateitem[2]+", scale: "+updateitem[3],id))
        mydb.commit()
    mycursor.execute("UPDATE events SET done = 1 WHERE  id = %s",(id,))
    mydb.commit()
    mycursor.execute("SELECT * FROM events WHERE done = 0")
    result = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    # print(result)
    return render_template('upcomming.html', data = result)

@app.route('/events/new_event', methods = ['POST','GET'])
def newevent():
    mydb = mysql.connector.connect(
    host = host,
    port= int(port),
    user = userdb,
    password = password, 
    database = dbname,
    use_pure=True
    )
    mycursor = mydb.cursor()
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        scale = request.form['scale']
        needed = request.form['needed']
        needed = int(needed) if needed else 1
        mycursor.execute("INSERT INTO events (title,descr,scale,members_needed) VALUES (%s,%s,%s,%s)",(title,desc,scale,needed))
        mydb.commit()
        mycursor.execute("SELECT * FROM events WHERE done = 0")
        result = mycursor.fetchall()
        return render_template('upcomming.html', data = result) 
    return render_template('newevent.html')

@app.route('/events/show_all')
def show_all():
    mydb = mysql.connector.connect(
    host = host,
    port= int(port),
    user = userdb,
    password = password, 
    database = dbname,
    use_pure=True
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM events ORDER BY done ASC, id ASC")
    result = mycursor.fetchall()
    return render_template('upcomming.html', data = result)

@app.route('/events/add_member/<id>')
def addcontibutor(id):
    mydb = mysql.connector.connect(
    host = host,
    port= int(port),
    user = userdb,
    password = password, 
    database = dbname,
    use_pure=True
    )
    mycursor = mydb.cursor()
    
    mycursor.execute("SELECT * FROM events WHERE id = %s",(id,))
    updateitem = mycursor.fetchone()
    if updateitem[5] == 0:
        # print("its not finished")
        mycursor.execute("UPDATE events SET cur_members = cur_members +1 WHERE id = %s",(id,))
        mydb.commit()
    else:
        print("item has already been finshed")
    mycursor.execute("SELECT * FROM events WHERE done = 0")
    result = mycursor.fetchall()
    return render_template('upcomming.html', data = result)


@app.route('/acomplishments')  # all pages dedaceded to the done page ------------------------------------------------------------------------------------
def done():
    mydb = mysql.connector.connect(
    host = host,
    port= int(port),
    user = userdb,
    password = password, 
    database = dbname,
    use_pure=True
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM done")
    result = mycursor.fetchall()
    fresult = []
    for items in result:
       thing = (items[0],items[1],items[2],items[3].isoformat(),items[4])
       fresult.append(thing)
    # print(result,fresult)
    return  render_template('done.html', data = fresult)

if __name__ == '__main__':
    app.run(debug =True)

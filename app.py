from flask import Flask, render_template, request
import mysql.connector
import sys
try:
    with open("password.txt","r")  as f:
        password = f.read()
except FileNotFoundError:
    print("password file doesnt exist")
app =Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/members')
def members():
    return "<h1> hello</h1>"


if __name__ == '__main__':
    app.run(debug =True)
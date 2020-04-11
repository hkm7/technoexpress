from app import app
from flask import render_template

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/signup') 
def signup():
    return render_template('signup.html')

@app.route('/home') 
def feed():
    return render_template('home.html')      
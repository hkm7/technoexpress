from flask import Flask,render_template, redirect, request  
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length

app= Flask(__name__)
app.config['SECRET_KEY']= "thisismysecretkey"

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(),Length(min=3,max=10)])
    password = PasswordField('password', validators=[InputRequired(),Length(min=8,max=20)])

@app.route('/',  methods = ['GET','POST'])
def root():
    return redirect('/home')
    
@app.route('/signup',methods = ['GET','POST']) 
def signup():
    return render_template('signup.html')

@app.route('/signup_process', methods=['POST'])
def signup_process():
    name = request.form[name]
    username = request.form[username]
    password = request.form[password]
    return redirect('/home')

@app.route('/login_process', methods=['POST'])
def login_process():
    username = request.form[uname]
    password = request.form[psw]]
    return redirect('/home')

@app.route('/login', methods = ['GET','POST']) 
def login():
    return render_template('login.html')

@app.route('/home', methods = ['GET','POST']) 
def home():
    return render_template('home.html')        




if __name__=='__main__':
    app.run(debug=True, port=3333)
    
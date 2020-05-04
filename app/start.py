from flask import Flask,render_template, redirect
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(),Length(min=3,max=10)])
    password = PasswordField('password', validators=[InputRequired(),Length(min=8,max=20)])

@app.route('/',  methods = ['GET','POST'])
def root():
    return render_template('home.html')
    
@app.route('/signup',methods = ['GET','POST']) 
def signup():
    return render_template('signup.html')

@app.route('/login', methods = ['GET','POST']) 
def feed():
    return render_template('login.html')
        

app= Flask(__name__)
app.config['SECRET_KEY']= "thisismysecretkey"



if __name__=='__main__':
    app.run(debug=True)
    
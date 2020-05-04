from app import app
from flask import Flask,render_template
from flask_wtf import Flaskform
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length


@app.route('/')
def root():
    return render_template('login.html')
    
@app.route('/signup') 
def signup():
    return render_template('signup.html')

@app.route('/login', methods = ['POST']) 
def feed():

    return render_template('home.html')      

app= Flask(__name__)
app.config['SECRET_KEY']= "thisismysecretkey"



if __name__=='__main__':
    app.run(debug=True)
    
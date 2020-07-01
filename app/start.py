from flask import Flask,render_template, redirect, request  
from flask_wtf import FlaskForm
import mysql.connector
from mysql.connector import Error
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length
from passlib.hash import sha256_crypt

app= Flask(__name__)
app.config['SECRET_KEY'] = "mysecretkey"

try:
    conn = mysql.connector.connect(host='localhost', database='technoexpress', user='root',password='')
    link = conn.cursor()
except:
    print("Error: Unable to connect to database!")
    


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(),Length(min=3,max=10)])
    password = PasswordField('password', validators=[InputRequired(),Length(min=8,max=20)])

class SignUpForm(FlaskForm):
    name = StringField('name', validators=[InputRequired()])
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
    form = SignUpForm(request.form)
    name = request.form[name]
    uname = request.form[usr]
    pwd = sha256_crypt.encrypt(request.form[pswd])
    try:
        link.execute("INSERT INTO userdata VALUES (NULL, "+name+", "+uname+", "+ pwd+");")
        return redirect('/home')
    except:
        print("Error username needs to be unique")
    

@app.route('/login_process', methods=['POST'])
def login_process():
    form = LoginForm(request.form)
    uname = request.form[username]
    pwd = request.form[password]
    try:
        tmp = link.execute("SELECT pwd FROM userdata WHERE uname="+uname+";")
        if(sha256_crypt.verify(pwd,tmp)):
            print("Login Successful!")
        else:
            print("Login failed: Check username/password!")    
    except:
        print("Error: Unable to login right now, please try again later")
        return redirect('/home')

@app.route('/login', methods = ['GET','POST']) 
def login():
    return render_template('login.html')

@app.route('/home', methods = ['GET','POST']) 
def home():
    link.execute("SELECT * FROM blogdata")
    result = link.fetchall()
    numrows = len(result)    
    return render_template('home.html', x=numrows,res=result)        




if __name__=='__main__':
    app.run(debug=True, port=3333)
    
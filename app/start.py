from flask import Flask,render_template, redirect, request  
from flask_wtf import FlaskForm
from flaskext.mysql import MySQL
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length
from passlib.hash import sha256_crypt

app= Flask(__name__)
app.config['SECRET_KEY'] = "mysecretkey"
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'technoexpress'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

try:
    conn = mysql.connect()
    link = conn.cursor()
except:
    print("Error: Unable to connect to database!")
    


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
    name = request.form[Name]
    uname = request.form[username]
    pwd = sha256_crypt.encrypt(request.form[password])
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
    return render_template('home.html')        




if __name__=='__main__':
    app.run(debug=True, port=3333)
    
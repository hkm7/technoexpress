from app import app
import sqlite3

conn=sqlite3.connect('technoexp.db')
c= conn.cursor()

def create_tables():
    c.execute("CREATE TABLE IF NOT EXISTS credentials(uid REAL, uname TEXT, pwd TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS feedContent(uid REAL, datestamp TEXT, title TEXT, content TEXT)")
    c.close()
    conn.close()

    
if __name__=='__main__':
    create_tables()
    app.run(debug=True)

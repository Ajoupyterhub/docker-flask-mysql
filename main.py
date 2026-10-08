from flask import Flask, request, jsonify, render_template
import pymysql

# docker exec -it mydb mysql -u root -p
# CREATE DATABASE todo CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

def get_db():
    return pymysql.connect(
        host='localhost', 
        port=33066,
        user= 'root',
        password= 'web1',
        database = 'todo',
        charset= 'utf8', 
        cursorclass=pymysql.cursors.DictCursor)

app = Flask(__name__)

def init_DB():
    try:
        conn = get_db()
        with conn.cursor() as cursor:
            sql = """
            CREATE TABLE IF NOT EXISTS todos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                is_complete BOOLEAN DEFAULT FALSE
            )
            """
            cursor.execute(sql)
        conn.commit()
    finally:
        conn.close()

init_DB()

@app.route('/')
def index():
    return render_template("index.html") #"Welcome to Todo Application"


if __name__ == "__main__":
    app.run(host='0.0.0.0')

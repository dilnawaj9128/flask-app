from flask import Flask, render_template, request, jsonify
import mysql.connector
import time

app = Flask(__name__)

def get_db_connection():
    while True:
        try:
            connection = mysql.connector.connect(
                host='db',
                user='root',
                password='password123',
                database='student_db'
            )
            return connection
        except mysql.connector.Error:
            print("Database connect ho raha hai...")
            time.sleep(5)

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        course VARCHAR(255)
    )
    """)

    conn.commit()
    conn.close()

@app.route("/")
def index():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name, course FROM students")
    students = cursor.fetchall()

    conn.close()

    return render_template("index.html", students=students)


@app.route("/add", methods=["POST"])
def submit():

    name = request.form.get("name")
    course = request.form.get("course")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, course) VALUES (%s,%s)",
        (name, course)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": f"{name} - {course} added!"})


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)

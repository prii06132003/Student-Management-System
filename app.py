from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "student_secret_key"

DB_NAME = "students.db"


# ---------------- DATABASE ----------------
def get_db():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        roll TEXT PRIMARY KEY,
        name TEXT,
        branch TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )
    """)

    # default login
    cur.execute("INSERT OR IGNORE INTO users VALUES (?, ?)", ("admin", "admin123"))

    conn.commit()
    conn.close()


# ---------------- LOGIN ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?",
                    (username, password))
        user = cur.fetchone()
        conn.close()

        if user:
            session["user"] = username
            return redirect("/dashboard")
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")

    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    conn.close()

    return render_template("index.html", students=students)


# ---------------- ADD STUDENT ----------------
@app.route("/add", methods=["POST"])
def add_student():
    if "user" not in session:
        return redirect("/")

    roll = request.form["roll"]
    name = request.form["name"]
    branch = request.form["branch"]

    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO students VALUES (?, ?, ?)", (roll, name, branch))
    conn.commit()
    conn.close()

    return redirect("/dashboard")


# ---------------- DELETE STUDENT ----------------
@app.route("/delete/<roll>")
def delete_student(roll):
    if "user" not in session:
        return redirect("/")

    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE roll=?", (roll,))
    conn.commit()
    conn.close()

    return redirect("/dashboard")


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# ---------------- RUN ----------------
if __name__ == "__main__":
    init_db()
    app.run(debug=True)

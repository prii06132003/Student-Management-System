import sqlite3

conn = sqlite3.connect("students.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll TEXT PRIMARY KEY,
    name TEXT,
    branch TEXT
)
""")

conn.commit()

def create_user_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )
    """)
    conn.commit()

def create_admin():
    cursor.execute("SELECT * FROM users WHERE username='admin'")
    if not cursor.fetchone():
        cursor.execute(
            "INSERT INTO users VALUES (?, ?)",
            ("admin", "admin123")
        )
        conn.commit()


def register_user(username, password):
    cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    conn.commit()

def login_user(username, password):
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return cursor.fetchone()


def add_student(roll, name, branch):
    cursor.execute("INSERT INTO students VALUES (?, ?, ?)", (roll, name, branch))
    conn.commit()

def get_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

def search_student(roll):
    cursor.execute("SELECT * FROM students WHERE roll=?", (roll,))
    return cursor.fetchone()

def update_student(roll, name, branch):
    cursor.execute("UPDATE students SET name=?, branch=? WHERE roll=?", (name, branch, roll))
    conn.commit()

def delete_student(roll):
    cursor.execute("DELETE FROM students WHERE roll=?", (roll,))
    conn.commit()

create_user_table()
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("users.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """)
    conn.close()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]

        conn = sqlite3.connect("users.db")
        conn.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()

    conn = sqlite3.connect("users.db")
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()

    return render_template("index.html", users=users)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("users.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """)
    conn.close()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]

        conn = sqlite3.connect("users.db")
        conn.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()

    conn = sqlite3.connect("users.db")
    users = conn.execute("SELECT * FROM users").fetchall()
    connclose()

    return render_template("index.html", users=users)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)

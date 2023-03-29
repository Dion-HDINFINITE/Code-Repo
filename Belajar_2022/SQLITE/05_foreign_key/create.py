import sqlite3

conn = sqlite3.connect("users.db")
cur = conn.cursor()

#check compability
cur.execute("""
    PRAGMA foreign_keys = ON
    """)

#table users
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE)
    """)

#table posts
cur.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        content TEXT NOT NULL DEFAULT "",
        FOREIGN KEY (user_id) REFERENCES users (id))

""")
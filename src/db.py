import sqlite3
import os

#database connection
def connect_db():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'library.db')
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

#initialize database tables
def init_db():
    conn = connect_db()
    c = conn.cursor()
    schema_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'schema.sql')

    f = open(schema_path, 'r')
    script = f.read()
    f.close()

    c.executescript(script)
    conn.commit()
    conn.close()

#book operations
def add_book(title, author, isbn, year, quantity):
    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO books (title, author, isbn, year, quantity) VALUES (?, ?, ?, ?, ?)",
              (title, author, isbn, year, quantity))
    conn.commit()
    conn.close()

def get_books():
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM books")
    rows = c.fetchall()
    conn.close()
    return rows

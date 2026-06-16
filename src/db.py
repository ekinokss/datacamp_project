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

def update_book(book_id, title, author, isbn, year, quantity):
    conn = connect_db()
    c = conn.cursor()
    c.execute("UPDATE books SET title=?, author=?, isbn=?, year=?, quantity=? WHERE id=?",
              (title, author, isbn, year, quantity, book_id))
    conn.commit()
    conn.close()

#delete a book by id
def delete_book(book_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    conn.close()

def search_books(keyword):
    conn = connect_db()
    c = conn.cursor()
    query = "SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ?"
    like = '%' + keyword + '%'
    c.execute(query, (like, like, like))
    result = c.fetchall()
    conn.close()
    return result

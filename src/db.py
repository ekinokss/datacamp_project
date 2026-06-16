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

#member stuff
def add_member(name, email, phone):
    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO members (name, email, phone) VALUES (?, ?, ?)",
              (name, email, phone))
    conn.commit()
    conn.close()

#get all members
def get_members():
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM members")
    rows = c.fetchall()
    conn.close()
    return rows

def update_member(member_id, name, email, phone):
    conn = connect_db()
    c = conn.cursor()
    c.execute("UPDATE members SET name=?, email=?, phone=? WHERE id=?", (name, email, phone, member_id))
    conn.commit()
    conn.close()

#delete member
def delete_member(member_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute("DELETE FROM members WHERE id=?", (member_id,))
    conn.commit()
    conn.close()

#loan a book
def borrow_book(book_id, member_id):
    conn = connect_db()
    c = conn.cursor()

    #check quantity
    c.execute("SELECT quantity FROM books WHERE id=?", (book_id,))
    row = c.fetchone()
    if row is None:
        conn.close()
        return False
    if row[0] <= 0:
        conn.close()
        return False

    c.execute("UPDATE books SET quantity = quantity - 1 WHERE id=?", (book_id,))
    c.execute("INSERT INTO loans (book_id, member_id, loan_date) VALUES (?, ?, date('now'))",
              (book_id, member_id))
    conn.commit()
    conn.close()
    return True

#return book
def return_book(loan_id):
    conn = connect_db()
    c = conn.cursor()

    c.execute("SELECT book_id FROM loans WHERE id=? AND returned=0", (loan_id,))
    row = c.fetchone()
    if row is None:
        conn.close()
        return False

    book_id = row[0]
    c.execute("UPDATE loans SET returned=1, return_date=date('now') WHERE id=?", (loan_id,))
    c.execute("UPDATE books SET quantity = quantity + 1 WHERE id=?", (book_id,))
    conn.commit()
    conn.close()
    return True

#get loans that arent returned yet
def get_active_loans():
    conn = connect_db()
    c = conn.cursor()
    c.execute("""SELECT l.id, b.title, m.name, l.loan_date
                 FROM loans l
                 JOIN books b ON l.book_id = b.id
                 JOIN members m ON l.member_id = m.id
                 WHERE l.returned = 0""")
    rows = c.fetchall()
    conn.close()
    return rows

#overdue check
def get_overdue_loans():
    conn = connect_db()
    c = conn.cursor()
    c.execute("""SELECT l.id, b.title, m.name, l.loan_date
                 FROM loans l
                 JOIN books b ON l.book_id = b.id
                 JOIN members m ON l.member_id = m.id
                 WHERE l.returned = 0 AND l.loan_date < date('now', '-14 days')""")
    rows = c.fetchall()
    conn.close()
    return rows

#all loans with book and member info
def get_all_loans():
    conn = connect_db()
    c = conn.cursor()
    c.execute("""SELECT l.id, b.title, m.name, l.loan_date, l.return_date, l.returned
                 FROM loans l
                 JOIN books b ON l.book_id = b.id
                 JOIN members m ON l.member_id = m.id""")
    rows = c.fetchall()
    conn.close()
    return rows

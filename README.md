# Library Management System

A CLI-based library management system built with Python and SQLite for the WAP 228 course.

## What It Does

This is a simple library system where you can manage books, members and book loans. All data is stored in an SQLite database. You can add/update/delete books and members, borrow and return books, and see which loans are active or overdue.

## How To Run

```bash
python -m src.main
```

Or:

```bash
cd src
python main.py
```

No extra libraries needed, just Python 3.

## Project Structure

```
├── db/
│   └── schema.sql        # database tables and sample data
├── src/
│   ├── __init__.py
│   ├── db.py             # database connection and all CRUD functions
│   ├── cli.py            # command line interface menus
│   └── main.py           # program entry point
├── tests/
│   └── test_crud.py      # unit tests for CRUD operations
└── README.md
```

## Database Design

3 tables:

- **books** - id, title, author, isbn, year, quantity
- **members** - id, name, email, phone, join_date
- **loans** - id, book_id (FK), member_id (FK), loan_date, return_date, returned

## How I Developed It

I started by designing the database schema. Then I wrote the db.py file for connecting to SQLite and doing CRUD operations. After that I built the CLI menus so users can interact with the system. Finally I added test cases and sample data.

The hardest parts were getting the JOIN queries right for loans and making the CLI work without bugs. I had to re-read the SQLite documentation a few times.

## What I Learned

- How to use SQLite with Python
- Writing CRUD operations with parameterized queries
- Using JOINs to combine data from multiple tables
- Building CLI applications with input/output loops
- Writing unit tests
- Using Git for version control

## Technologies

- **Python** - the programming language, handles all logic and user interaction
- **SQL** - for storing and querying data, defining relationships between tables
- **Git/GitHub** - version control, tracking changes throughout development

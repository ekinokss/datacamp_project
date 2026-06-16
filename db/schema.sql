-- library database schema

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    isbn TEXT UNIQUE,
    year INTEGER,
    quantity INTEGER DEFAULT 1
);

CREATE TABLE members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    join_date TEXT DEFAULT (date('now'))
);

CREATE TABLE loans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    member_id INTEGER,
    loan_date TEXT DEFAULT (date('now')),
    return_date TEXT,
    returned INTEGER DEFAULT 0,
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (member_id) REFERENCES members(id)
);

-- sample data for testing
INSERT INTO books (title, author, isbn, year, quantity) VALUES
('1984', 'George Orwell', '9780451524935', 1949, 3),
('To Kill a Mockingbird', 'Harper Lee', '9780061120084', 1960, 2),
('The Great Gatsby', 'F. Scott Fitzgerald', '9780743273565', 1925, 5),
('Pride and Prejudice', 'Jane Austen', '9780141439518', 1813, 1),
('Sapiens', 'Yuval Noah Harari', '9780062316097', 2011, 4),
('Dune', 'Frank Herbert', '9780441172719', 1965, 2),
('Clean Code', 'Robert C. Martin', '9780132350884', 2008, 3);

INSERT INTO members (name, email, phone) VALUES
('Ahmet Yilmaz', 'ahmet@example.com', '555-0101'),
('Ayse Demir', 'ayse@example.com', '555-0102'),
('Mehmet Kaya', 'mehmet@example.com', '555-0103'),
('Zeynep Celik', 'zeynep@example.com', '555-0104');

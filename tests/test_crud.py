import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src import db

#test crud operations
class TestLibraryCRUD(unittest.TestCase):

    def setUp(self):
        #use test db
        db_path = os.path.join(os.path.dirname(__file__), '..', 'test_library.db')
        self.conn = db.connect_db()
        self.conn.close()
        #hack to use test db
        self.old_connect = db.connect_db
        def test_connect():
            c = __import__('sqlite3').connect(db_path)
            c.execute("PRAGMA foreign_keys = ON")
            return c
        db.connect_db = test_connect
        db.init_db()

    def tearDown(self):
        db.connect_db = self.old_connect
        db_path = os.path.join(os.path.dirname(__file__), '..', 'test_library.db')
        if os.path.exists(db_path):
            os.remove(db_path)

    #test adding a book
    def test_add_book(self):
        db.add_book("test book", "test author", "1234567890", 2023, 5)
        books = db.get_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0][1], "test book")

    #test updating a book
    def test_update_book(self):
        db.add_book("old title", "old author", "1111111111", 2020, 2)
        books = db.get_books()
        bid = books[0][0]
        db.update_book(bid, "new title", "new author", "2222222222", 2024, 3)
        updated = db.get_books()
        self.assertEqual(updated[0][1], "new title")
        self.assertEqual(updated[0][4], 2024)

    def test_delete_book(self):
        db.add_book("delete me", "someone", "3333333333", 2019, 1)
        books = db.get_books()
        bid = books[0][0]
        db.delete_book(bid)
        remaining = db.get_books()
        self.assertEqual(len(remaining), 0)

    def test_search_books(self):
        db.add_book("python basics", "john doe", "4444444444", 2022, 2)
        db.add_book("java basics", "jane doe", "5555555555", 2021, 1)
        res = db.search_books("python")
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0][1], "python basics")

    def test_add_member(self):
        db.add_member("test user", "test@test.com", "555-0000")
        members = db.get_members()
        self.assertEqual(len(members), 1)
        self.assertEqual(members[0][1], "test user")

    def test_borrow_and_return(self):
        db.add_book("borrowable", "author", "6666666666", 2023, 2)
        db.add_member("borrower", "b@test.com", "555-1111")
        bid = db.get_books()[0][0]
        mid = db.get_members()[0][0]

        ok = db.borrow_book(bid, mid)
        self.assertTrue(ok)

        books = db.get_books()
        self.assertEqual(books[0][5], 1) #quantity decreased

        loans = db.get_active_loans()
        self.assertEqual(len(loans), 1)

        lid = loans[0][0]
        ok = db.return_book(lid)
        self.assertTrue(ok)

        books = db.get_books()
        self.assertEqual(books[0][5], 2) #quantity restored

    def test_borrow_no_stock(self):
        db.add_book("rare book", "author", "7777777777", 2023, 0)
        db.add_member("desperate", "d@test.com", "555-2222")
        bid = db.get_books()[0][0]
        mid = db.get_members()[0][0]
        ok = db.borrow_book(bid, mid)
        self.assertFalse(ok)


if __name__ == '__main__':
    unittest.main()

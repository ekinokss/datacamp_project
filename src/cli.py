from src import db
import sys

#main screen
def main_menu():
    while True:
        print("")
        print("===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Books")
        print("2. Members")
        print("3. Loans")
        print("4. Exit")
        c = input("choose > ")

        if c == "1":
            book_menu()
        elif c == "2":
            print("not done yet")
        elif c == "3":
            print("not done yet")
        elif c == "4":
            print("goodbye")
            sys.exit(0)
        else:
            print("wrong choice try again")

#book menu
def book_menu():
    while True:
        print("")
        print("--- Books ---")
        print("1. Add book")
        print("2. List all books")
        print("3. Update book")
        print("4. Delete book")
        print("5. Search books")
        print("6. Back")

        ch = input("choose > ")

        if ch == "1":
            title = input("title: ")
            author = input("author: ")
            isbn = input("isbn: ")
            year = input("year: ")
            qty = input("quantity: ")
            if title == "" or author == "":
                print("title and author required")
                continue
            try:
                yr = int(year) if year else 0
                qt = int(qty) if qty else 1
            except:
                print("year and quantity must be numbers")
                continue
            db.add_book(title, author, isbn, yr, qt)
            print("book added")

        elif ch == "2":
            books = db.get_books()
            if len(books) == 0:
                print("no books found")
            for b in books:
                print("ID:{} | {} by {} | isbn:{} | year:{} | qty:{}".format(b[0], b[1], b[2], b[3], b[4], b[5]))

        elif ch == "3":
            bid = input("book id to update: ")
            try:
                bid = int(bid)
            except:
                print("id must be number")
                continue
            title = input("new title: ")
            author = input("new author: ")
            isbn = input("new isbn: ")
            year = input("new year: ")
            qty = input("new quantity: ")
            try:
                yr = int(year) if year else 0
                qt = int(qty) if qty else 1
            except:
                print("year and quantity must be numbers")
                continue
            db.update_book(bid, title, author, isbn, yr, qt)
            print("updated")

        elif ch == "4":
            bid = input("book id to delete: ")
            try:
                bid = int(bid)
            except:
                print("id must be number")
                continue
            db.delete_book(bid)
            print("deleted")

        elif ch == "5":
            kw = input("search keyword: ")
            res = db.search_books(kw)
            if len(res) == 0:
                print("nothing found")
            for b in res:
                print("ID:{} | {} by {} | isbn:{} | year:{} | qty:{}".format(b[0], b[1], b[2], b[3], b[4], b[5]))

        elif ch == "6":
            break
        else:
            print("invalid option")
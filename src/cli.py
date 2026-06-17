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
            member_menu()
        elif c == "3":
            loan_menu()
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

#member menu
def member_menu():
    while True:
        print("")
        print("--- Members ---")
        print("1. Add member")
        print("2. List members")
        print("3. Update member")
        print("4. Delete member")
        print("5. Back")

        ch = input("choose > ")

        if ch == "1":
            name = input("name: ")
            email = input("email: ")
            phone = input("phone: ")
            if name == "":
                print("name cant be empty")
                continue
            db.add_member(name, email, phone)
            print("member added")

        elif ch == "2":
            members = db.get_members()
            if len(members) == 0:
                print("no members")
            for m in members:
                print("ID:" + str(m[0]) + " | " + m[1] + " | email:" + str(m[2]) + " | phone:" + str(m[3]) + " | joined:" + str(m[4]))

        elif ch == "3":
            mid = input("member id: ")
            try:
                mid = int(mid)
            except:
                print("id must be number")
                continue
            name = input("new name: ")
            email = input("new email: ")
            phone = input("new phone: ")
            db.update_member(mid, name, email, phone)
            print("updated")

        elif ch == "4":
            mid = input("member id to delete: ")
            try:
                mid = int(mid)
            except:
                print("id must be number")
                continue
            db.delete_member(mid)
            print("deleted")

        elif ch == "5":
            break
        else:
            print("invalid")

#loan menu
def loan_menu():
    while True:
        print("")
        print("--- Loans ---")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. Active loans")
        print("4. Overdue loans")
        print("5. All loans")
        print("6. Back")

        ch = input("choose > ")

        if ch == "1":
            try:
                bid = int(input("book id: "))
                mid = int(input("member id: "))
            except:
                print("ids must be numbers")
                continue
            ok = db.borrow_book(bid, mid)
            if ok:
                print("book borrowed")
            else:
                print("borrow failed check ids or quantity")

        elif ch == "2":
            try:
                lid = int(input("loan id: "))
            except:
                print("id must be number")
                continue
            ok = db.return_book(lid)
            if ok:
                print("book returned")
            else:
                print("return failed check loan id")

        elif ch == "3":
            loans = db.get_active_loans()
            if len(loans) == 0:
                print("no active loans")
            for l in loans:
                print(f"loan#{l[0]} | {l[1]} | borrowed by {l[2]} on {l[3]}")

        elif ch == "4":
            overdue = db.get_overdue_loans()
            if len(overdue) == 0:
                print("no overdue loans")
            for l in overdue:
                print("OVERDUE loan#{} | {} | {} since {}".format(l[0], l[1], l[2], l[3]))

        elif ch == "5":
            all_loans = db.get_all_loans()
            if len(all_loans) == 0:
                print("no loans")
            for l in all_loans:
                status = "returned" if l[5] else "active"
                print(f"loan#{l[0]} | {l[1]} | {l[2]} | {l[3]} | {l[4]} | {status}")

        elif ch == "6":
            break
        else:
            print("invalid")
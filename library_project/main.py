from book import Book
from borrower import Borrower
from library import Library
from loan import Loan
from librarian import Librarian
from persistence_manager import PersistenceManager
option = input("Enter choice: ")  
def menu():
    print(""" =============================
     SCHOOL LIBRARY SYSTEM
=============================

BOOKS
1. View all books
2. Search books
3. Add book

BORROWERS
4. View borrowers
5. Register borrower

LOANS
6. Issue loan
7. Return book
8. View active loans

DATA
9. Save data
10. Load data

0. Exit""")

menu()

if option == "1":
    pass
elif option == "2": 
    Library.search_by_title()
elif option == "3":
    Librarian.add_book()
elif option == "4":
    Library()
elif option == "5":
    Library.register_borrower()
elif option == "6":
    Librarian.issue_loan() 
elif option == "7":
    Librarian.accept_return
    Loan.mark_returned()
    Book.mark_available()
elif option == "8":
    Borrower.list_current_loans()
elif option == "9":
    PersistenceManager.save_library()
elif option == "10":
    PersistenceManager.load_library()
elif option == "0":
    import sys
    sys.exit(0) #exits the system
else: #catch all
    ()
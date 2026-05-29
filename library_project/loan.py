from datetime import datetime as date, datetime, timedelta

class Loan():
    def __init__(self, book, borrower, borrow_date, due_date, returned):
        self.book = book
        self.borrower = borrower
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.returned = returned

    def mark_returned():
        pass

    def is_overdue():
        borrow_period = 21
        due_date = timedelta(day = (borrow_period))
        if date.today() > due_date:
            return True

    def calculate_fine():
        if .is_overdue == True:


from datetime import datetime as date, datetime, timedelta

class Loan():
    def __init__(self, book, borrower, borrow_date, due_date, returned):
        self.book = book
        self.borrower = borrower
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.returned = returned

    def mark_returned(self):
        self.returned = True #set returned to returned 

    def is_overdue(self):
        borrow_period = timedelta(days = (21))  #selts the amount of time borrowable to 21
        self.due_date = borrow_period + self.borrow_date #set due date to day borrowed + 21 days
        if self.returned == True: #if the book is returned
            return False #book is not overdue
        elif date.today() > self.due_date: #if book is currently borrowed, and today is after the due date
            return True #book is overdue


    def calculate_fine(self, fine_per_day=0.50): #sets fine to 50c per day
        if self.is_overdue(): #if is_overdue = true (?)
            days_overdue = (date.today() - self.due_date) #check amount of days it is over due by
            return days_overdue * fine_per_day #returns a fine amount of the amount of days overdue multiplied by the fine per day
        return 0.0 #if there is no fine, then return nothing :3            
class Borrower():
    def __init__(self, name, borrower_id):
        self.name = name
        self.borrower_id = borrower_id
        self.loans = []

    def add_loan(self, loan):
        self.loans.append(loan) #when they borrow something/loan something add the book to their list of loans

    def list_current_loans(self):
        print(f"Borrower: {self.name} (ID: {self.borrower_id})") #format for loan display
        for loan in self.loans:
            loan.display() #display all loans

    def has_overdue_loans(self):
        for loan in self.lones: #for every loan they have in their loan list
            if loan.is_overdue(): #check if the loan is overdue
                return True #if any book is overdue, return that they do have overdue books
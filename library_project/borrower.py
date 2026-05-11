class Borrower():
    def __init__(self, name, borrower_id):
        self.name = name
        self.borrower_id = borrower_id
        self.loans = []

    def add_loan(self, loan):
        self.loans.append(loan)

    def list_current_loans(self):
        print(f"Borrower: {self.name} (ID: {self.borrower_id})")
        for loan in self.loans:
            loan.display()

    def has_overdue_loans(self):
        for loan in self.lones:
            if loan.is_overdue():
                overdue = True
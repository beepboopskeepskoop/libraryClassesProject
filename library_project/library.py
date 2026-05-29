class Library():
    def __init__(self, name):
        self.name = name
        self.books = []
        self.borrowers = []
        self.loans = []
        self.librarians = []

    def add_book(self, book):
        pass

    def register_borrower(self, borrower):
        pass

    def create_loan(self, borrower, book):
        pass

    def return_book(self, loan):
        pass    

    def search_by_title(self, title):
        print("yay")

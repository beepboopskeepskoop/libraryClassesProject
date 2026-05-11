class Book():
    def __init__(self, book_id, title, author, date):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.date = date

    def display(self):
        print(f"ID - {self.book_id}")
        print(f"TITLE - {self.title}")
        print(f"AUTHOR - {self.author}")
        print(f"BORROWED - {self.borrowed}")
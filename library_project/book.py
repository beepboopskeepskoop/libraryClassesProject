class Book():
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = None

    def mark_available(self):
        self.available = True
        return

    def mark_unavailable(self):
        self.available = False
        return
    
    def is_available(self):
        if self.available == True:
            return self
        else: 
            print("error")
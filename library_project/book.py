class Book():
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = None

    def mark_available(self):
        return self.available == True
    
    def mark_unavailable(self):
        return self.available == False
    
    def is_available(self):
        pass
        
x = Book("Hello", "Testing", 123)
Book.mark_available(x)
Book.is_available(x)
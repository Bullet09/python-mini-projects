class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display_info(self):
        print(
            f"\nTitle: {self.title} \nAuthor: {self.author} \nAvailable: {self.available} \n")

    def borrow(self):
        if self.available == True:
            print("You can borrow the book")
            self.available = False
        elif self.available == False:
            print("Book is not available")
            return

    def return_book(self):
        if self.available == False:
            print("Book returned!")
            self.available = True
        elif self.available == True:
            print("Book is already available")


class Library:
    books = []

    def __init__(self, books):
        self.books = books


book1 = Book("Python Crash Course", "Eric Matthes")
book1.display_info()

book2 = Book("Harry Potter", "J.K. Rowling")
book2.display_info()

book3 = Book("Marvel", "Stan Lee")
book3.display_info()

book1.return_book()
book1.display_info()
book1.borrow()
book1.display_info()

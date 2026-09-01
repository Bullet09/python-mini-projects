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

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for i in self.books:
            i.display_info()

    def find_book(self, title):

        for i in self.books:
            if i.title == title:
                i.display_info()


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

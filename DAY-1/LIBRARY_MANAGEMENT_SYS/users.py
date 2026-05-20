class User:

    def __init__(self, name):
        self.name = name
        self.books_taken = []

    def take_book(self, book):
        self.books_taken.append(book.title)

    def return_book(self, book):
        self.books_taken.remove(book.title)
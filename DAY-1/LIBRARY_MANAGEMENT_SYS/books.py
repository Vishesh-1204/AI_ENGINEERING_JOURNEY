class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

    def issue_book(self):
        self.is_issued = True

    def return_book(self):
        self.is_issued = False
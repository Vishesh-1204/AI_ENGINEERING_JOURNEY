from books import Book
from users import User


book1 = Book("Atomic Habits", "James Clear")

user1 = User("Vishesh")


book1.issue_book()

user1.take_book(book1)


print(book1.title)
print(book1.is_issued)

print(user1.books_taken)

from book import Book
from patron import Patron
from librarian import Librarian
from library import Library

# Create books
book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1122334455")

# Create patrons
patron1 = Patron("Alice", "P001")
patron2 = Patron("Bob", "P002")

# Create librarian
librarian = Librarian("Eve", "L001")

# Create library
library = Library("Central Library")

# Librarian adds books to the library
librarian.add_book(library, book1)
librarian.add_book(library, book2)
librarian.add_book(library, book3)

# Librarian adds patrons to the library
librarian.add_patron(library, patron1)
librarian.add_patron(library, patron2)

# Patron borrows a book
patron1.borrow_book(book1)
patron1.borrow_book(book2)

# Patron returns a book
patron1.return_book(book1)

# List all books and patrons in the library
print("Books in the library:")
for book in library.list_books():
    print(book)

print("\nPatrons in the library:")
for patron in library.list_patrons():
    print(patron)

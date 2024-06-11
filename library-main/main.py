
from book import Book
from patron import Patron
from librarian import Librarian
from library import Library

# Create books
book1 = Book("Dead Poets Society", "Nancy H. Kleinbaum", "3134567987")
book2 = Book("La Dame Aux Camelias", "Alexandre Dumas", "8554613479")
book3 = Book("White nights", " Fyodor Dostoevsky", "7897875641")

# Create patrons
patron1 = Patron("Jack", "P001")
patron2 = Patron("Anna", "P002")

# Create librarian
librarian = Librarian("Giorgina", "L001")

# Create library
library = Library("Bibliothèque François-Mitterrand")

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

print("Patrons in the library:")
for patron in library.list_patrons():
    print(patron)

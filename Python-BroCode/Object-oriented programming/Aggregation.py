
# Aggregation = Represents a relationship where one object (the whole)
#       contains references to one or more INDEPENDENT objects (the parts)

class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def books_list(self):
        return [f"{book.title}  by  {book.author}" for book in self.books]

class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author

library = Library("Madia National Library")

book1 = Book(title="Shahi Al Bukhari", author="H. B. Bukhari")
book2 = Book(title="Tafsir Ibn Kathir", author="Inb. Kathir")
book3 = Book(title="The Fine Necture", author="Mobarak Puri (RH)")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)
print()
for i, book in enumerate(library.books_list()):
    print(f"{i + 1}.{book}")
    print()
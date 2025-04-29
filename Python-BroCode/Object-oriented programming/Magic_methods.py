
# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
# They are automatically called by many of Python's built-in operations.
# They allow developers to define or customize the behavior of objects

class Book:
    
    def __init__(self, title, author, pages) -> None:
        self.title = title
        self.author = author
        self.pages = pages


    def __str__(self) -> str:
        return f"{self.title} by {self.author}, Pages : {self.pages}"


    def __eq__(self, other) -> bool:
        return(
            self.title == other.title 
            or self.author == other.author 
            or self.pages == other.pages
            )
    
  
    def __gt__(self, other) -> bool:
        return (
            'Will take long' if self.pages > other.pages 
            else 'Won''t take long'
            )


    def __lt__(self, other) -> bool:
        return self.pages < other.pages


    def __add__(self, other) -> str:
        return self.pages + other.pages


    def __contains__(self, keyword) -> bool:
        return keyword in self.title or keyword in self.author


    def __getitem__(self, key) -> str:
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'pages':
            return self.pages
        else:
            return f"'{key}' not found !"


book1 = Book(title="The Hobbit", author="J.R.R. Tolkien", pages=310)
book2 = Book(title="Harry Potter and The Philosopher's Stone", author="J.K. Rowling", pages=223)
book3 = Book(title="The Lion, the Witch and the Wardrobe", author="C.S. Lewis", pages=172)


print(book1)
print(book2)
print(book3) #__str__

print(book1 == book2) #__eq__
print(book3 > book2) #__gt__
print(book1 < book2) #__lt__
print(book1 + book2) #__add__
print("Lion" in book3) #__contains__

print(book1['title'])
print(book2['author'])  #__getitem__
print(book3['pages'])
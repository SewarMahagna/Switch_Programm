class Book:
    def __init__(self, title, authors, genre, year, **kwargs):
        self.title = title
        self.authors = authors
        self.genre = genre
        self.year = year
        self.additional_info = kwargs

    def __repr__(self):
        return (f"Book(title={self.title}, authors={self.authors}, genre={self.genre}, "
                f"year={self.year}, additional_info={self.additional_info})")


class BookManager:
    def __init__(self):
        self.books_by_title = {}  
        self.books_by_author = {}  

    def add_book(self, book):

        self.books_by_title[book.title] = book
        for author in book.authors:
            if author not in self.books_by_author:
                self.books_by_author[author] = []
            self.books_by_author[author].append(book)

    def find_by_title(self, title):
        return self.books_by_title.get(title, None)

    def find_by_author(self, author):
        return self.books_by_author.get(author, [])

book1 = Book("Book A", ["James"], "Fiction", 2020, ISBN="123456789")
book2 = Book("Book B", ["James", "Roz"], "Non-Fiction", 2018, Copies=10)
book3 = Book("Book C", ["Rami", "Sami"], "Fantasy", 2021)

manager = BookManager()
manager.add_book(book1)
manager.add_book(book2)
manager.add_book(book3)

print(manager.find_by_title("Book A"))
print(manager.find_by_author("James"))
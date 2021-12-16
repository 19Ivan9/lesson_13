# Не совсем ещё понял по поводу __repr__ и __str__ в плане правильного использования
# но всё подучу и буду уверенно их использовать, а пока, весь тот коричневатый с кусочками орешков код работает)
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []
        self.book_count = 0

    def __repr__(self):
        return f'{self.name} have {self.book_count} books:{self.books}'

    def __str__(self):
        return f'{self.name} have {self.book_count} books:{self.books}'

    def new_book(self, book, author):
        self.book_count += 1
        self.books.append(book)
        self.authors.append(author)
        author.author_books.append([book.name, book.year])

    def group_by_author(self, author):
        for a in self.authors:
            if a == author:
                return author.author_books


    def group_by_year(self, year):
        for book in self.books:
            if book.year == year:
                return book


class Book:
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        self.book = []

    def __repr__(self):
        self.book = [self.name, self.year, self.author]
        return f'Book info : {self.book}'

    def __str__(self):
        self.book = [self.name, self.year, self.author]
        return f'Book info : {self.book}'


class Author:
    def __init__(self, name, country, bd):
        self.name = name
        self.country = country
        self.bd = bd
        self.info = []
        self.author_books = []

    def __repr__(self):
        self.info = [self.name, self.country, self.bd]
        return f'Author info:{self.info}'

    def __str__(self):
        self.info = [self.name, self.country, self.bd]
        return f'Author info:{self.info}'

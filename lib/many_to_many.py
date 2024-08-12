class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return[contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, cur_author):
        if not isinstance(cur_author, Author):
            raise Exception("author property should be an instance of the Author class")
        self._author = cur_author

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, cur_book):
        if not isinstance(cur_book, Book):
            raise Exception("book property should be an instance of the Book class")
        self._book = cur_book

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, cur_date):
        if not isinstance(cur_date, str):
            raise Exception("date property should be a string")
        self._date = cur_date

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, cur_royalties):
        if not isinstance(cur_royalties, int):
            raise Exception("royalties property should be an integer")
        self._royalties = cur_royalties

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

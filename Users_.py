from Person_ import *
from Books_ import *



class Users(Person):

    def __init__(self, name, firstName, pwd):
        super().__init__(name, firstName, pwd)
        self.rank = 0
        self.borrow = []

    def Borrow(self, book):
        self.book = book.getTitle()
        self.borrow.append(book)

    def BackTo(self, book):
        self.book = book.getTitle()
        self.borrow.remove(book)

    def __repr__(self):
        affiche = f"{self.name} {self.firstName} son identifiant est {self.id} son rang est de {self.rank} il a emprunté {self.borrow}"
        return affiche



user2 = Users("HArry", "Potter", "ksqfhioreahoier")

user2.Borrow(book1)
print(user2)
user2.BackTo("KAKA")
print(user2)
from Person_ import *

class Users(Person):

    def __init__(self, name, firstName, pwd):
        super().__init__(name, firstName, pwd)
        self.rank = 0
        self.borrow = []

    def Borrow(self, book):
        self.borrow.append(book)

    def BackTo(self, book):
        self.borrow.pop(book)

    def __repr__(self):
        affiche = f"{self.name} {self.firstName} son identifiant est {self.id} son rang est de {self.rank}"
        return affiche

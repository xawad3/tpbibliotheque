from Person_ import *
from Books_ import *



class Users(Person):

    def __init__(self, name, firstName, pwd):
        super().__init__(name, firstName, pwd)
        # counter est égal au nombre de fois où l'user a rendu un livre, 
        # le rank se base sur ce nombre pour définir une valeur (10 retours = +1 rank)
        self.rank = 0
        self.counter = 0
        self.borrow = []

    def rank_up(self):
        if self.counter < 10:
            self.rank = 0
        elif self.counter > 100:
            self.rank = "10, Rang Max"
        else:
            self.rank = len(self.counter)[0]

    def Borrow(self):
        self.book = book.getTitle()
        self.borrow.append(book)

    def BackTo(self, book):
        self.book = book.getTitle()
        self.borrow.remove(book)
        self.counter =+ 1

    def __repr__(self):
        affiche = f"{self.name} {self.firstName} son identifiant est {self.id} son rang est de {self.rank} il a emprunté {self.borrow}"

        return affiche



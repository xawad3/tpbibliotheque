from Person_ import *
from Books_ import *



class Users(Person):

    def __init__(self, name_user, first_name_user, pwd):
        super().__init__(name_user, first_name_user, pwd)
        # counter est égal au nombre de fois où l'user a rendu un livre, 
        # le rank se base sur ce nombre pour définir une valeur (10 retours = +1 rank)
        self.rank = 0
        #self.sub = None
        #self.counter_rank = 0
        self.borrow = []

    # def Rank_up(self):
    #     if self.counter_rank < 10:
    #         self.rank = 0
    #     elif self.counter_rank > 100:
    #         self.rank = "10, Rang Max"
    #     else:
    #         self.rank = int(str(self.counter_rank)[0])


    def Borrow(self, ref):
        self.borrow.append(ref)

    def BackTo(self, book):
        self.borrow.remove(book.getRef())
        self.counter_rank += 1

    def __repr__(self):
        affiche = f"{self.name_user} {self.first_name_user} son identifiant est {self.id} son rang est de {self.rank} il a emprunté {self.borrow} son mdp {self.pwd}"

        return affiche



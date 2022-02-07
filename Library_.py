from Users_ import *

class Library:

    def __init__(self, name):
        self.name = name
        self.section = []
        self.author = []
        self.books = []
        self.users = []

    def __repr__(self):
        choix = input(f"Ouvrages contenu dans la bibliothèque {self.name}:\nTapez 1 pour l'affichage par catégorie\nTapez 2 pour l'affichage par auteur\n")
        if choix == 1:
            affiche = f"Voici la liste des livres, triés par catégorie: {self.section}"
        if choix == 2:
            affiche = f"Voici la liste des livres, triés par auteurs: {self.author}"

    def getName(self):
        return self.name

    def add_a_book(self):
        with open("list_books.txt", 'a') as f:
            f.write(self)

    def remove_a_book(self):
        with open("list_books.txt", "r+") as f:
            f.truncate(self)

    def add_user(self, user):
        with open("list_users.txt", "a") as f:
            maChaine = user.name + ";" + user.firstName + ";" + user.id + "." + str(user.rank) + ";" + user.borrow
            f.write(maChaine)

    def remove_user(self):
        with open("list_users.txt", "r+") as f:
            f.truncate(self)
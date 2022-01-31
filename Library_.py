from Books_ import *
from Comic_strip import *
from Users_ import *
from Person_ import *

class Library:

    def __init__(self, name):
        self.name = name
        self.section = []
        self.author = []
        self.books = []
        self.users = []
        
    def __repr__(self):
        choix = input(f"Ouvrages contenu dans la bibliothèque {self.name}:\nTapez "1" pour l'affichage par catégorie\nTapez "2" pour l'affichage par auteur\n")
        if choix == 1:
            affiche = f"Voici la liste des livres, triés par catégorie: {self.section}\n"
        elif choix == 2:
            affiche = f"Voici la liste des livres, triés par auteurs: {self.author}\n"

    def getName(self):
        return self.name

    def add_a_book(self, book):
        self.books.append(self)
        with open("list_books.txt", 'a') as f:
            f.write(book)

    def remove_a_book(self, book):
        self.books.remove(self)
        with open("list_books.txt", "r+") as f:
            f.truncate(book)

    def add_user(self):
        self.users.append(self)
        with open("list_users.txt", "a") as f:
            f.write(self)

    def remove_user(self):
        self.users.remove(self)
        with open("list_users.txt", "r+") as f:
            f.truncate(self)
from Books_ import *
from Comic_strip import *


class Library:

    def __init__(self, name):
        self.name = name
        self.section = []
        self.author = []
        self.books = []
        self.users = []
        
    def __repr__(self):
        choix = int(input(f"Ouvrages contenu dans la bibliothèque {self.name}:\nTapez "1" pour l'affichage par catégorie\nTapez "2" pour l'affichage par auteur"))
        if choix = 1:
            affiche = f"Voici la liste des livres, triés par catégorie: {self.section}"
        if choix = 2:
            affiche = f"Voici la liste des livres, triés par auteurs: {self.author}"
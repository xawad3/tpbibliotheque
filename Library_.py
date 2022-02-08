from Users_ import *
from Books_ import *
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

    def add_a_book(self, b):
        self.books.append(b)
        
    def export_books(self):
        with open('list_books.txt', 'w') as f:
            for item in self.books:
                f.write(str(item.title) +" ; "+ str(item.author) +" ; "+ str(item.language) +" ; "+ str(item.category) +" ; "+ str(item.ref)+"\n")

    def import_books(self):
        with open("list_books.txt", 'r') as f:
            for line in f:
                #importer les elements line.title etc... et ensuite append l'objet
                self.books.append(line)

    def add_user(self, user):
        with open("list_users.txt", "a") as f:
            maChaine = user.name + ";" + user.firstName + ";" + user.id + ";" + str(user.rank) + ";" + str(user.borrow)
            f.write(maChaine)

    def remove_user(self, user):
        with open("list_users.txt", "r+") as f:

            maChaine = user.name + ";" + user.firstName + ";" + user.id + "." + str(user.rank) + ";" + user.borrow
            f.truncate(maChaine)

biblio = Library("ABC")
biblio.add_a_book(book1)
biblio.add_a_book(book2)
biblio.add_a_book(book3)
biblio.export_books()

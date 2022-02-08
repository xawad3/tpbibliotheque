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
            for item in f:
                maLigne = item.split(" ; ")
                print(maLigne)
                self.books.append(Books(maLigne[0],maLigne[1],maLigne[2],maLigne[3],maLigne[4]))
                if maLigne[1] not in self.author:
                    self.author.append(maLigne[1])
                if maLigne[3] not in self.section:
                    self.section.append(maLigne[3])
                # it works, reste à eviter les doublons
                

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
biblio.add_a_book(book4)
biblio.add_a_book(book5)
biblio.export_books()
input("on vient d'exporter la liste en .txt\" maintenant efface la liste self.books et fait l'import")
biblio.books = []
input("normalement la liste self.books est vide")
print(biblio.books)
input("je viens d'afficher la liste books, maintenant je lance l'import depuis txt")
biblio.import_books()
input("maintenant je tente d'afficher juste les auteurs")
print(biblio.author)
input("et là les catégories")
print(biblio.section)
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

    def export_user(self, user):
        with open("list_users.txt", "a") as f:
            maChaine = user.name + " ; " + user.firstName + " ; " + user.id + " ; " + str(user.rank) + " ; " + str(user.borrow) + " ; " + str(user.counter)
            if maChaine not in f:
                f.write(maChaine)

    def import_user(self):
        with open("list_users.txt", 'r') as f:
            for item in f:
                maLigne = item.split(" ; ")
                print(maLigne)
                self.users.append(Users(maLigne[0],maLigne[1],maLigne[2]))
                self.users[-1].rank = maLigne[3]
                for i in (maLigne[-1])[1:-1].split(","):
                    self.users[-1].borrow.append(i)
                self.users[-1].counter = maLigne[4]


    #def remove_user(self, user):
        #with open("list_users.txt", "r+") as f:
            #f.truncate(maChaine)
biblio = Library("OK")
biblio.import_user()
input("on vient d'exporter la liste en .txt\" maintenant efface la liste self.books et fait l'import")
biblio.user = []
input("normalement la liste self.books est vide")
print(biblio.books)
input("je viens d'afficher la liste books, maintenant je lance l'import depuis txt")
biblio.export.user()
input("maintenant je tente d'afficher juste les auteurs")
print(biblio.author)
input("et là les catégories")
print(biblio.section)

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
                f.write(str(item.title) +" ; "+ str(item.author) +" ; "+ str(item.language) +" ; "+ str(item.type) +" ; "+ str(item.category) +" ; "+ str(item.ref)"\n")

    def import_books(self):
        with open("list_books.txt", 'r') as f:
            for item in f:
                maLigne = item.split(" ; ")
                self.books.append(Books(title=maLigne[0],author=maLigne[1],language=maLigne[2],type=maLigne[3],category=maLigne[4],ref=maLigne[5]))
                if maLigne[1] not in self.author:
                    self.author.append(maLigne[1])
                if maLigne[3] not in self.section:
                    self.section.append(maLigne[3])
                self.books[-1].ref = maLigne[5]
            
                

    def search_author_list(self):
        pass

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


  


from Users_ import *
from Books_ import *
class Library:

    def __init__(self, name_library):
        self.name_library = name_library
        self.section_list = []
        self.author_list = []
        self.books_list = []
        self.users_list = []

    def __repr__(self):
        choix = input(f"Ouvrages contenu dans la bibliothèque {self.name_library}:\nTapez 1 pour l'affichage par catégorie\nTapez 2 pour l'affichage par auteur\n")
        if choix == 1:
            affiche = f"Voici la liste des livres, triés par catégorie: {self.section_list}"
        if choix == 2:
            affiche = f"Voici la liste des livres, triés par auteurs: {self.author_list}"

    def getName(self):
        return self.name_library

    def add_a_book(self, b):
        self.books_list.append(b)
        
    def export_books(self):
        with open('list_books.txt', 'w') as f:
            for item in self.books_list:
                f.write(str(item.title_book) +" ; "+ str(item.author_book) +" ; "+ str(item.language_book) +" ; "+ str(item.type_book) +" ; "+ str(item.category_book) +" ; "+ str(item.ref_book) + "\n")
                pass

    def import_books(self):
        with open("list_books.txt", 'r') as f:
            for item in f:
                maLigne = item.split(" ; ")
                self.books_list.append(Books(title_book=maLigne[0],author_book=maLigne[1],language_book=maLigne[2],type_book=maLigne[3],category_book=maLigne[4],ref_book=maLigne[5]))
                if maLigne[1] not in self.author_list:
                    self.author_list.append(maLigne[1])
                if maLigne[3] not in self.section_list:
                    self.section_list.append(maLigne[3])
                self.books_list[-1].ref = maLigne[5]
            
                

    def search_author_list(self):
        pass

    def export_users(self):
        with open('list_users.txt', 'w') as f:
            for item in self.users_list:
                f.write(str(item.name_user) + " ; " + str(item.first_name_user) + " ; " + str(
                    item.pwd) + " ; " + str(item.rank) + " ; " + str(item.counter_rank) + " ; " + str(
                    item.borrow) + "\n")

    def import_user(self):
        with open("list_users.txt", 'r') as f:
            for item in f:
                maLigne = item.split(" ; ")
                print(maLigne)
                self.users_list.append(Users(maLigne[0],maLigne[1],maLigne[2]))
                self.users_list[-1].rank = maLigne[3]
                for i in (maLigne[-1])[1:-1].split(","):
                    self.users_list[-1].borrow.append(i)
                self.users_list[-1].counter = maLigne[4]

    def object_by_ref(self, ref):
        for i in self.books_list:
            if ref == i.ref_book:
                return i


  


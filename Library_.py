from Users_ import *
from Books_ import *
from functions import *
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

# Pour Créer (ajouter) un livre dans books_list
# =============================================
    def add_a_book(self, b):
        self.books_list.append(b)
        
# Exportation des livres contenus dans books_list => list_books.txt
# =================================================================
    def export_books(self):
        with open('list_books.txt', 'w', encoding="utf-8") as f:
            for item in self.books_list:
                f.write(str(item.title_book) +" ; "+ str(item.author_book) +" ; "+ str(item.language_book) +" ; "+ str(item.type_book) +" ; "+ str(item.category_book) +" ; "+ str(item.ref_book) +" ; "+ str(item.dispo)+ " ; " + str(item.backto) + "\n")

# Importation des livres du .txt => books_list
# ============================================
    def import_books(self):
        with open("list_books.txt", 'r', encoding="utf-8") as f:
            for item in f:
                maLigne = item.split(" ; ")
                self.books_list.append(Books(title_book=maLigne[0],author_book=maLigne[1],language_book=maLigne[2],type_book=maLigne[3],category_book=maLigne[4]))
                self.books_list[-1].ref_book = maLigne[5]
                #self.books_list[-1].dispo = maLigne[6]
                if maLigne[1] not in self.author_list:
                    self.author_list.append(maLigne[1])
                if maLigne[4] not in self.section_list:
                    self.section_list.append(maLigne[4])
                self.books_list[-1].ref = maLigne[5]

                if maLigne[6] == "True":
                    self.books_list[-1].dispo = True
                    self.books_list[-1].backto = None

                elif maLigne[6] == "False":
                    self.books_list[-1].dispo = False
                    date_hour = datetime.datetime.strptime(maLigne[7][:-1], "%Y-%m-%d")
                    self.books_list[-1].backto = datetime.datetime.date(date_hour)

            
# Affiche la liste des auteurs dans l'ordre alphabétique
# ======================================================
    def search_author_list(self):
        # author_temp_list = []
        # for i in self.books_list:
        #     author_temp_list.append(i.author_book)
        #     author_temp_list.sort()
        self.author_list = sorted(self.author_list)
        Menu(self.author_list)

# Affiche la liste des Livres par ordre alphabétique
# ==================================================
    def search_books_list(self):
        books_temp_list = []
        for i in self.books_list:
            books_temp_list.append(i.title_book)
            books_temp_list.sort()
        Menu(books_temp_list)

# Affichage des livres par auteur
# ===============================
    def books_by_author(self, x):
        author = []
        for i in self.books_list:
            if x.lower() in i.author_book.lower():
                if not i.author_book in author:
                    author.append(i.author_book)
        if len(author) > 1:
            Menu(author)
            choix = input("Choisissez votre auteur(le numéro)")
            auteur_choix = author[int(choix)]
            self.books_by_author(auteur_choix)

        else:
            for i in self.books_list:
                if i.author_book == author[0]:
                    print(i.title_book + " : " + i.ref_book)

    def books_by_title(self, x):
        title = []
        for i in self.books_list:
            if x.lower() in i.title_book.lower():
                title.append(i.title_book + " : " + i.ref_book)
        Menu(title)


    def books_by_type(self, x):
        type = []
        for i in self.books_list:
            if x.lower() in i.type_book.lower():
                type.append(i.title_book + " : " + i.ref_book)
        Menu(type)

    def books_by_category(self, x):
        category = []
        for i in self.books_list:
            if x.lower() in i.category_book.lower():
                category.append(i.title_book + " : " + i.ref_book)
        Menu(category)

    def books_by_language(self, x):
        language = []
        for i in self.books_list:
            if x.lower() in i.language_book.lower():
                language.append(i.title_book + " : " + i.ref_book)
        Menu(language)

    def export_users(self):
        with open('list_users.txt', 'w', encoding="utf-8") as f:
            for item in self.users_list:
                f.write(item.name_user + " ; " + item.first_name_user + " ; " +
                    item.pwd + " ; " + str(item.rank) + " ; " + str(item.id) + " ; " + str(
                    item.borrow) + "\n")


    def import_user(self):
        with open("list_users.txt", 'r', encoding="utf-8") as f:
            for item in f.readlines():
                maLigne = item.split(" ; ")

                self.users_list.append(Users(maLigne[0], maLigne[1], maLigne[2]))
                self.users_list[-1].rank = int(maLigne[3])
                self.users_list[-1].id = maLigne[4]
                #print(self.users_list[-1])
                listeEmpruntTempo = maLigne[-1][1:-2]

                if len(listeEmpruntTempo) == 0:
                    self.users_list[-1].borrow = []
                else:
                    for i in (listeEmpruntTempo.split(", ")):
                        self.users_list[-1].borrow.append(i[1:-2])

                #self.users_list[-1].counter = maLigne[5]



    def object_by_ref(self, ref):
        for i in self.books_list:
            if ref == i.ref_book:
                return i

    def object_by_title(self, ref):
        for i in self.books_list:
            if ref == i.ref_book:
                return i.title_book





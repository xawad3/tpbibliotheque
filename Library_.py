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
            maChaine = user.name + " ; " + user.firstName + " ; " + user.id + " ; " + str(user.rank) + " ; " + str(user.borrow)
            if maChaine not in f:
                f.write(maChaine)

    # def remove_user(self, user):
    #     with open("list_users.txt", "r+") as f:

    #         maChaine = user.name + ";" + user.firstName + ";" + user.id + "." + str(user.rank) + ";" + user.borrow
    #         f.truncate(maChaine)

biblio = Library("ABC")
biblio.add_a_book(book1)
biblio.add_a_book(book2)
biblio.add_a_book(book3)
biblio.add_a_book(book4)
biblio.add_a_book(book5)
biblio.export_books()
print(biblio.books[0].ref)
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


maLigne = "m.prybylo;maxime;przybylo;Azerty77;999999;[HJ1924893,AR9248837]"  
mesEmprunts = []  
#maLigne.split(";") permet de créer une liste en divisant ma chaine de caractère par ";" 
#maLigne.split(";")[-1] permet de recupérer la derniere "case" en tant que str 
#maLigne.split(";")[-1][1:-1] permet de ne garder que du deuxieme caractère (inclus) au dernier (non inclus) 
#le dernier split permet de créer une liste en divisant mes ref par "," 
for i in (maLigne.split(";")[-1])[1:-1].split(","):     
  mesEmprunts.append(i)  
  print(mesEmprunts)
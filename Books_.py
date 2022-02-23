import random
import datetime
import locale

locale.setlocale(locale.LC_TIME, '')

class Books:

    def __init__(self, title_book, author_book, language_book, type_book, category_book):
        self.title_book = title_book
        self.author_book = author_book
        self.language_book = language_book
        self.type_book = type_book #roman, nouvelles etc
        self.category_book = category_book #fantastique, polar etc
        self.ref_book = (title_book[0] + author_book[0] + str(random.randint(0, 100000))).lower()
        self.dispo = True
        self.backto = None

    def getRef(self):
        return self.ref_book

    def getNameBook(self):
        return self.title_book

    def noDispo(self):
        self.dispo = False

    def Dispo(self):
        self.dispo = True

    def returnBookDate(self):
        self.backto = None


    def dateBackto(self):
        self.backto = datetime.date.today() + datetime.timedelta(days=15)
        return datetime.date.strftime(self.backto, "%A %d %B %Y")

    def extendBorrow(self, days):
        self.backto = self.backto + datetime.timedelta(days=days)
        return self.backto


    def __repr__(self):
        # if self.dispo == True :
        affiche = (f"Le livre {self.title_book} de l'auteur {self.author_book}, réfèrence {self.ref_book} est disponible à l'emprunt\n")
        # else :
        # affiche = (f"Le livre {self.title_book} de l'auteur {self.author_book}, réfèrence {self.ref_book} n'est pas disponible à l'emprunt\n")
        return affiche



book1 = Books("Une Fois trois", "Axelle AUclair", "Français", "Roman D'amour", "Roman")
book2 = Books("Maudite", "C. Sizel", "Français", "Fantasy", "Roman")
book3 = Books("Au café de la ville perdue", "Anaïs Llobet", "Français", "Littérature Française", "Roman")
book4 = Books("Légendes et contes traditionnels de l'Inde", "Catherine Clément", "Français", "Non-Fiction", "Roman")
book5 = Books("Nouvelles histoires extraordinaires", "Edgar Allan Poe", "Français", "Fantastique", "Nouvelles")
book6 = Books("Poésies Complètes", "Arthur Rimbaud", "Français", "Littérature", "Poèmes")
book7 = Books("Numéro 2", "David Foenkinos", "Français", "Drame", "Roman")
book8 = Books("La décision", "Karine Tuil", "Français", "Témoignage", "Roman")
book9 = Books("Anéantir", "Michel Houellebecq", "Français", "Anticipation", "Roman")
book10 = Books("Celui qui veille la nuit", "Louise Erdrich", "Français", "Roman Historique", "Roman")
book12 = Books("Celui qui veille la nuit", "Louise Rimbaud", "Français", "Roman Historique", "Roman")
print(book1)


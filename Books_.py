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

    def getMyDispo(self):

        if self.dispo == True:
            dispoOn = '\033[32m' #j'initialise ma couleur
            dispoOff = '\033[0m' #je reinitialise ma couleur
            return (dispoOn + "est disponible à l'emprunt" + dispoOff)
        else:
            dispoOn = '\033[91m' #j'initialise ma couleur
            dispoOff = '\033[0m' #je reinitialise ma couleur
            return (dispoOn + f'''n'est pas disponible à l'emprunt mais devrait revenir le {datetime.date.strftime(self.backto, "%A %d %B %Y")}''' + dispoOff)

    def dateBackto(self):
        self.backto = datetime.date.today() + datetime.timedelta(days=15)
        return datetime.date.strftime(self.backto, "%A %d %B %Y")

    def extendBorrow(self, days):
        self.backto = self.backto + datetime.timedelta(days=days)
        return datetime.date.strftime(self.backto, "%A %d %B %Y")


    def __repr__(self):
        if self.dispo == True :
            affiche = f'''Le livre "{self.title_book}" de l'auteur "{self.author_book}", réfèrence {self.ref_book} est disponible à l'emprunt\n'''
        else :
            affiche = f'''Le livre "{self.title_book}" de l'auteur "{self.author_book}", réfèrence {self.ref_book} qui n'est plus disponible à l'emprunt qui devrait être de retour {datetime.date.strftime(self.backto, "%A %d %B %Y")}\n'''
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
book13 = Books("Harry Potter à l'école des sorciers", "JK Rowling", "Français", "Fantastique", "Roman")
book14 = Books("Harry Potter et la Chambre des Secrets", "JK Rowling", "Français", "Fantastique", "Roman")
book15 = Books("Harry Potter et le Prisonnier d'Azkaban", "JK Rowling", "Français", "Fantastique", "Roman")

book20 = Books("Les Contes de Beedle le Barde", "Beedle le Barde", "Anglais", "Contes pour enfants", "Nouvelles")
book21 = Books("Les Contes du Champignons", "Beatrix Bloxam", "Anglais", "Contes pour enfants", "Nouvelles")
book22 = Books("Rencontre enchantées", "Fifi LaFolle", "Français", "Roman d'amour", "Roman")
book23 = Books("Ma Vie de Moldue", "Daisy Hookum", "Anglais", "Autobiographie", "Autobiographie")
book24 = Books("Magical Waters Plants of the Highlands Lochs", "Hadrian Whittle", "Anglais", "Botanique", "Roman")
book25 = Books("Guide to Household Pests", "Gilderoy Lockhart", "Anglais", "Aventures", "Roman")
book26 = Books("Travels with Trolls", "Gilderoy Lockhart", "Anglais,", "Aventures", "Romans")
book27 = Books("Comment ensorceler son fromage", "Greta Grandamour", "Français", "Recettes", "Cuisine")



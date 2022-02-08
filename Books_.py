import random



class Books:

    def __init__(self, title, author, language, type, category):
        self.title = title
        self.author = author
        self.language = language
        self.type = type
        self.category = category
        self.ref = title[0] + author[0] + str(random.randint(0, 100000))
        self.dispo = True
        self.backto = None

    def getTitle(self):
        return self.title

    def __repr__(self):
        affiche = f"Le livre {self.title} de l'auteur {self.author} en {self.language} du genre {self.type} de la catégorie {self.category} est enregistré sous la référence {self.ref}\n"
        return affiche



book1 = Books("Une Fois trois", "Axelle AUclair", "Français", "Roman D'amour", "Roman")
book2 = Books("Maudite", "C. Sizel", "Français", "Fantasy", "Roman")
book3 = Books("Au café de la ville perdue", "Anaïs Llobet", "Français", "Littérature Française", "Roman")
# book4 = Books("Légendes et contes traditionnels de l'Inde", "Catherine Clément", "Français", "Non-Fiction", "Roman")
# book5 = Books("Nouvelles histoires extraordinaires", "Edgar Allan Poe", "Français", "Fantastique", "Nouvelles")
# book6 = Books("Poésies Complètes", "Arthur Rimbaud", "Français", "Littérature", "Poèmes")
# book7 = Books("Numéro 2", "David Foenkinos", "Français", "Drame", "Roman")
# book8 = Books("La décision", "Karine Tuil", "Français", "Témoignage", "Roman")
# book9 = Books("Anéantir", "Michel Houellebecq", "Français", "Anticipation", "Roman")
# book10 = Books("Celui qui veille la nuit", "Louise Erdrich", "Français", "Roman Historique", "Roman")
print(book1)


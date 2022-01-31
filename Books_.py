import random
from Users_ import *

class Books:
    def __init__(self, title, author, language, type, category):
        self.title = title
        self.author = author
        self.language = language
        self.type = type
        self.category = category
        self.ref = title[0]+author[0]+str(random.randint(0,100000))
        self.dispo = True
        self.backto = None

    def __repr__(self):
        affiche= f"Le livre {self.title} de l'auteur {self.author} en {self.language} du genre {self.type} de la catégorie {self.category} est enregistré sous la référence {self.ref}\n"
        return affiche

book1 = Books("Rama", "Kdik", "english", "SF", "novell")
print (book1)
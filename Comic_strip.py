from Books_ import *

class ComicStrip(Books) :
    def __init__(self, title, author, language, type, category,color, artist):
        super().__init__(self, title, author, language, type, category)
        self.color = color
        self.artist = artist

    def __repr__(self):
        affiche= f"Le livre {self.title} de l'auteur {self.author} en {self.language} du genre {self.type} de la catégorie {self.category} est une bande déssinée en {self.color} dessinée par {self.artist}\n"
        return affiche



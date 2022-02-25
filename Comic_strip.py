from Books_ import *


class ComicStrip(Books):

    def __init__(self, title_book, author_book, language_book, type_book, category_book , color_comic , artist_comic):
        super().__init__(title_book, author_book, language_book, type_book, category_book)
        self.color_comic = color_comic
        self.artist_comic = artist_comic

    def __repr__(self):
        affiche = f"Le livre {self.title_book} de l'auteur {self.author_book} en {self.language_book} du genre {self.type_book} de la catégorie {self.category_book} est une bande déssinée en {self.color_comic} dessinée par {self.artist_comic}\n"
        return affiche


bd1 = ComicStrip("Huntr 2-La brousse", "Jordan Morris", "Français", "Aventure", "BD",True,"Himself")
bd2 = ComicStrip("Akira","Otomo Katsuhiro", "Français", "Anticipation", "BD",False, "Otomo Katsuhiro")
bd3 = ComicStrip("Atar Gull ou le destin d'un esclave modèle","Fabien Nury", "Français", "Adaptation", "BD",True, "Laurence Croix")

print(bd1)

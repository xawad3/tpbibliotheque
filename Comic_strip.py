from Books_ import *


class ComicStrip(Books):

    def __init__(self, title, author, language, type, category,color,artist):
        super().__init__(title, author, language, type, category)
        self.color = True
        self.color = color
        self.artist = artist

    def __repr__(self):
        affiche = f"Le livre {self.title} de l'auteur {self.author} en {self.language} du genre {self.type} de la catégorie {self.category} est une bande déssinée en {self.color} dessinée par {self.artist}\n"
        return affiche


bd1 = ComicStrip("Huntr 2-La brousse", "Jordan Morris", "Français", "Aventure", "BD",True,"Himself")
# bd2 = ComicStrip("Akira","Otomo Katsuhiro", "Français", "Anticipation", "BD",False, "Otomo Katsuhiro")
# bd3 = ComicStrip("Atar Gull ou le destin d'un esclave modèle","Fabien Nury", "Français", "Adaptation", "BD",True, "Laurence Croix")

print(bd1)

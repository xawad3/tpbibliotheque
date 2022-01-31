from Books_ import *

class ComicStrip(Books) :
    def __init__(self, title, author, language, type, category,color, artist):
        super().__init__(self, title, author, language, type, category)
        self.color = color
        self.artist = artist

    def __repr__(self):
        affiche = f"Le livre {self.title} de l'auteur {self.author} en {self.language} du genre {self.type} de la catégorie {self.category} est une bande déssinée en {self.color} dessinée par {self.artist}\n"
        return affiche


bd1 = ComicStrip("Huntr 2-La brousse","Jordan Morris", "Français", "Aventure", "BD","Couleur", "Tony Cliff")
bd2 = ComicStrip("Akira","Otomo Katsuhiro", "Français", "Anticipation", "BD","N&B", "Otomo Katsuhiro")
bd3 = ComicStrip("Atar Gull ou le destin d'un esclave modèle","Fabien Nury", "Français", "Adaptation", "BD","Couleur", "Laurence Croix")

# Print(bd1)


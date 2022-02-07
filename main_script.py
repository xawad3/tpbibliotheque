from functions import *
from Person_ import *
from Library_ import *



choice = ["Rechercher un livre", "Créer un compte", "Se connecter"]

print("Bienvenue dans la bibliothèque (le nom ?)")



while True:
    Menu(choice)
    entry = int(input("Que voulez-vous faire ?"))
    ###----début enregistrement d'un utilisateur----###
    if entry == 1:
        name = input("Quel est votre nom ?\n")
        first_name = input("Quel est votre prénom ?\n")
        encore = True
        while encore:
            pwd = input("Choisissez un mot de passe: \n")

            if len(pwd) < 5:
                print("Attention, votre mot de passe doit contenir au moins cinq caractères !")

            else:
                encore = False
                new = Person(name, first_name, pwd)
                Library.add_user(new.getMyName())







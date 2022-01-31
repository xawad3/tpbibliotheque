from Person_ import *
from Library_ import *
from Users_ import *



###----début enregistrement d'un utilisateur----###

print("Bienvenue dans la bibliothèque (le nom)")
again = True
while again:

    inscrire = input("Voulez-vous vous inscrire ? o/n")
    if inscrire == "o":
        name = input("Quel est votre nom ?\n")
        first_name = input("Quel est votre prénom ?\n")
        encore = True
        while encore:
            pwd = input("Choisissez un mot de passe: \n")

            if len(pwd) < 5:
                print("Votre mot de passe doit contenir au moins cinq caractères !")

            else:
                encore = False
                new = Person(name, first_name, pwd)

        print(new)




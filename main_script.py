from functions import *
from Person_ import *
from Library_ import *
from Users_ import *



choice = ["Rechercher un livre", "Créer un compte", "Se connecter"]
biblio = Library("Pourdlard")

print("Bienvenue dans la bibliothèque", biblio.name)



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
                new = Users(name, first_name, pwd)
                biblio.users.append(new)
                biblio.add_user(new)

    print(biblio.users)

    if entry == 2:
        is_Loged = False
        logUser = input("Veuillez entrer votre log-in")
        for i in biblio.users:
            if logUser == i.id:
                psdUser = input("Veuillez entrer votre mdp")
                if psdUser == i.pwd:
                    print("Connexion réussie")
                    is_Loged = True










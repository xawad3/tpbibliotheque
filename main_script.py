from functions import *
from Person_ import *
from Library_ import *
from Users_ import *



choice = ["Rechercher un livre", "Créer un compte", "Se connecter"]
choice1 = ["Rechercher un livre", "Emprunter un livre", "Prolonger un emprunt", "Se déconnecter"]
biblio = Library("Pourdlard")

print("Bienvenue dans la bibliothèque", biblio.name)


inscrire = True
while inscrire:
    Menu(choice)
    entry = int(input("Que voulez-vous faire ?"))
    ###----début enregistrement d'un utilisateur----###
    if entry == 0:
        print("La fonctionnalité 'recherche un livre' n'est pas encore disponible ! Bientôt !")
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
                print("Votre compte utilisateur a été créé, voici votre identifiant", new.id, "prenez soin de le noter !")
                biblio.users.append(new)
                biblio.add_user(new)
    ###----fin enregistrement d'un utilisateur----###


    print(biblio.users)


    ###----début connexion d'un utilisateur----###
    if entry == 2:
        inscrire = False
        is_Loged = False
        logUser = input("Veuillez entrer votre log-in")
        for i in biblio.users:
            if logUser == i.id:
                psdUser = input("Veuillez entrer votre mdp")
                if psdUser == i.pwd:
                    print("Connexion réussie")
                    is_Loged = True
    ###----fin connexion d'un utilisateur----###
                    Menu(choice1)
                    entry1 = int(input("Que voulez-vous faire ?"))
                    if entry1 == 0:
                        print("La fonctionnalité 'rechercher un livre'  n'est pas encore disponible ! Bientôt !")

                    if entry1 == 1:
                        print("La fonctionnalité 'emprunter un livre'  n'est pas encore disponible ! Bientôt !")

                    if entry == 2:
                        print("La fonctionnalité 'prolonger un emprunt'  n'est pas encore disponible ! Bientôt !")

                    else:
                        print("Vous êtes déconnectez")














from functions import *
from Person_ import *
from Library_ import *
from Users_ import *
from Books_ import *



choice = ["Rechercher un livre", "Créer un compte", "Se connecter"]
choice1 = ["Rechercher un livre", "Emprunter un livre", "Prolonger un emprunt", "Changer votre mot de passe", "Se déconnecter"]
biblio = Library("Pourdlard")
user1 = Users("Potter", "Harry", "drago")
biblio.users.append(user1)
user1.Borrow(book1)
print(user1)


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
        pwd = input("Choisissez un mot de passe: \n")
        #test = longeurmdp(pwd)
        while not longeurmdp(pwd):

            pwd = input("Choisisser un mot de passe")


        new = Users(name, first_name, pwd)
        print("Votre compte utilisateur a été créé, voici votre identifiant", new.id, "prenez soin de le noter !")
        biblio.users.append(new)
        biblio.export_user(new)
    ###----fin enregistrement d'un utilisateur----##

    print(biblio.users)

    ###----début connexion d'un utilisateur----###
    if entry == 2:
        inscrire = False
        connexion = True
        logUser = input("Veuillez entrer votre log-in")
        psdUser = input("Veuillez entrer votre mdp")
        compteur = 0
        while not verif_user(biblio.users, logUser, psdUser):
            compteur += 1
            print("Identifiant ou mot de passe incorrect !")
            logUser = input("Veuillez entrer votre log-in")
            psdUser = input("Veuillez entrer votre mdp")
            if compteur > 2:
                connexion = False
                print("Trop de fois")
                break

        if connexion:
            print("Connexion réussie")

    ###----fin connexion d'un utilisateur----###
            infini = True
            Menu(choice1)
            entry1 = int(input("Que voulez-vous faire ?"))
            if entry1 == 0:
                print("La fonctionnalité 'rechercher un livre'  n'est pas encore disponible ! Bientôt !")

            if entry1 == 1:
                print("La fonctionnalité 'emprunter un livre'  n'est pas encore disponible ! Bientôt !")

            if entry1 == 2:
                print("La fonctionnalité 'prolonger un emprunt'  n'est pas encore disponible ! Bientôt !")

            if entry1 == 3:
                changement = True
                mdp = input("Entrez votre mot mot de passe actuel")
                compteur  = 0
                while not verif_user(biblio.users, logUser, mdp):
                    compteur += 1
                    mdp = input("Entrez votre mot mot de passe actuel")
                    if compteur > 2:
                        changement = False
                        print("Au revoir !")
                        break
                if changement:
                    new_mdp = input("Entrez votre nouveau mot de passe")
                    changement_mdp(biblio.users, logUser, new_mdp)
                    print("Changement mdp réussi")


            else:
                print("Vous êtes déconnectez")





print(user1)








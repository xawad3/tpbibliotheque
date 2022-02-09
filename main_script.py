from functions import *
from Person_ import *
from Library_ import *
from Users_ import *




choice = ["Rechercher un livre", "Créer un compte", "Se connecter"]
choice1 = ["Rechercher un livre", "Emprunter un livre", "Prolonger un emprunt", "Changer votre mot de passe", "Se déconnecter"]
biblio = Library("Pourdlard")
user1 = Users("Potter", "Harry", "drago")
biblio.users_list.append(user1)
user1.Borrow(book1)
print(user1)


print("Bienvenue dans la bibliothèque", biblio.name_library)

inscrire = True
while inscrire:
    Menu(choice)
    entry = input("Que voulez-vous faire ?")

    try:
        entry = int(entry)
    except ValueError:
        ok = False
        print("Veuillez entrer un chiffre")
    else:
        ok = True

    while ok:
        ###----début enregistrement d'un utilisateur----###
        if entry == 0:
            print("La fonctionnalité 'recherche un livre' n'est pas encore disponible ! Bientôt !")
        elif entry == 1:
            name = input("Quel est votre nom ?\n")
            first_name = input("Quel est votre prénom ?\n")
            pwd = input("Choisissez un mot de passe: \n")
            #test = longeurmdp(pwd)
            while not longeurmdp(pwd):

                pwd = input("Votre mot de passe doit faire au moins 5 caractères veuillez retaper un mot de passe")


            new = Users(name, first_name, pwd)
            print("Votre compte utilisateur a été créé, voici votre identifiant", new.id, "prenez soin de le noter !")
            biblio.users_list.append(new)
            biblio.export_users()
        ###----fin enregistrement d'un utilisateur----##



        ###----début connexion d'un utilisateur----###
        elif entry == 2:
            inscrire = False
            connexion = True
            logUser = input("Veuillez entrer votre log-in")
            psdUser = input("Veuillez entrer votre mdp")
            compteur = 0
            while not verif_user(biblio.users_list, logUser, psdUser):
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


                infini = True
                while infini:
                    Menu(choice1)
                    entry = input("Que voulez-vous faire ?")
                    try:
                        entry = int(entry)
                    except ValueError:
                        ok = False
                        print("Veuillez entrer un chiffre")
                    else:
                        ok = True

                    while ok:
                        if entry == 0:
                            print("La fonctionnalité 'rechercher un livre'  n'est pas encore disponible ! Bientôt !")

                        elif entry == 1:
                            print("La fonctionnalité 'emprunter un livre'  n'est pas encore disponible ! Bientôt !")

                        elif entry == 2:
                            print("La fonctionnalité 'prolonger un emprunt'  n'est pas encore disponible ! Bientôt !")

                        elif entry == 3:
                            changement = True
                            mdp = input("Entrez votre mot mot de passe actuel")
                            compteur  = 0
                            while not verif_user(biblio.users_list, logUser, mdp):
                                compteur += 1
                                mdp = input("Entrez votre mot mot de passe actuel")
                                if compteur > 2:
                                    changement = False
                                    print("Au revoir !")
                                    break
                                if changement:
                                    new_mdp = input("Entrez votre nouveau mot de passe")
                                    changement_mdp(biblio.users_list, logUser, new_mdp)
                                    print("Changement mdp réussi")


                        else:
                            infini = False
                            print("Vous êtes déconnectez")
                            inscrire = True


                ###----fin connexion d'un utilisateur----###

        elif entry >= 3:
            print("Veuillez faire un choix présent dans la liste")
            ok = False



#print(user1)
#print(biblio.users_list)








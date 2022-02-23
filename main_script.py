# from dbm.ndbm import library
from functions import *
from Person_ import *
from Library_ import *
from Users_ import *
import time




choice = ["Rechercher un livre", "Créer un compte", "Se connecter", "J'ai perdu mes identifiants"]
choice1 = ["Rechercher un livre", "Emprunter un livre", "Prolonger un emprunt", "Rendre un livre", "Changer votre mot de passe", "Se déconnecter"]
choice2 = ["Par auteur", "Par genre", "Par catégorie", "Par titre", "Par langue", "Revenir au menu précédent"]

biblio = Library("Pourdlard")

# Ajout de livre dans la biblio pour la matière
biblio.add_a_book(book1)
biblio.add_a_book(book2)
biblio.add_a_book(book3)
#

user1 = Users("Potter", "Harry", "drago")
biblio.users_list.append(user1)
biblio.add_a_book(book1)
biblio.add_a_book(book2)
biblio.add_a_book(book3)
biblio.add_a_book(book4)
biblio.add_a_book(book5)
biblio.add_a_book(book6)
biblio.add_a_book(book7)
biblio.add_a_book(book8)
biblio.add_a_book(book12)
print(user1)

print("————————————————————————————————————")
print("Bienvenue dans la bibliothèque", biblio.name_library)
print("————————————————————————————————————")

inscrire = True
while inscrire:
    Menu(choice)
    entry = input("Que voulez-vous faire ?\n")

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
            Menu(choice2)
            choix = int(input("Comment souhaitez vous rechercher votre livre ?\n"))
            if choix == 0:
                biblio.books_by_author(input("Ecrivez le nom de l'auteur\n"))

            elif choix == 1:
                biblio.books_by_type(input("Ecrivez le nom de du genre\n"))

            elif choix == 2:
                biblio.books_by_category(input("Ecrivez le nom de la catégorie\n"))

            elif choix == 3:
                biblio.books_by_title(input("Ecrivez le titre du livre\n"))

            else:
                biblio.books_by_language(input("Ecrivez la langue du livre\n"))
        elif entry == 1:
            name = input("Quel est votre nom ?\n")
            first_name = input("Quel est votre prénom ?\n")
            pwd = input("Choisissez un mot de passe: \n")
            #test = longeurmdp(pwd)
            while not longeurmdp(pwd):

                pwd = input("Votre mot de passe doit faire au moins 5 caractères veuillez retaper un mot de passe correct.\n")

            print("Un instant nous vérifions vos informations ...")
            print("————————————————————————————————————")
            time.sleep(1)
            new = Users(name, first_name, pwd)
            print("Félicitations votre compte utilisateur a été créé, voici votre identifiant", new.id, "prenez soin de le noter !")
            print("————————————————————————————————————")
            biblio.users_list.append(new)
            biblio.export_users()
            ok = False
        ###----fin enregistrement d'un utilisateur----##



        ###----début connexion d'un utilisateur----###
        elif entry == 2:
            inscrire = False
            connexion = True
            logUser = input("Veuillez entrer votre log-in\n")
            psdUser = input("Veuillez entrer votre mdp\n")
            print("Un instant nous vérifions vos informations ...")
            print("————————————————————————————————————")
            time.sleep(1)
            compteur = 0
            while not verif_user(biblio.users_list, logUser, psdUser):
                compteur += 1
                print("Identifiant ou mot de passe incorrect !")
                logUser = input("Veuillez entrer votre log-in\n")
                psdUser = input("Veuillez entrer votre mdp\n")
                if compteur > 2:
                    connexion = False
                    print("Vous avez rentrée un id ou un mdp erroné trop de fois, veuillez contacter un administrateur pour récupérer vos identifiants !")
                    break

            if connexion:
                for users in biblio.users_list:
                    if logUser == users.id:
                        connected_user = users
                print("Connexion réussie")
                print("————————————————————————————————————")


                infini = True
                while infini:
                    Menu(choice1)
                    entry = input("Que voulez-vous faire ?\n")
                    try:
                        entry = int(entry)
                    except ValueError:
                        ok = False
                        print("Veuillez entrer un chiffre\n")
                    else:
                        ok = True

                    while ok:
                        if entry == 0:
                            Menu(choice2)
                            choix = int(input("Comment souhaitez vous rechercher votre livre ?\n"))
                            if choix == 0:
                                biblio.books_by_author(input("Ecrivez le nom de l'auteur\n"))

                            elif choix == 1:
                                biblio.books_by_type(input("Ecrivez le nom de du genre\n"))

                            elif choix == 2:
                                biblio.books_by_category(input("Ecrivez le nom de la catégorie\n"))

                            elif choix == 3:
                                biblio.books_by_title(input("Ecrivez le titre du livre\n"))

                            elif choix == 4:
                                biblio.books_by_language(input("Ecrivez la langue du livre\n"))

                            else:
                                ok = False




                        # Fonctionnalité Emprunter un livre
                        elif entry == 1:
                            print(f"Voici la liste des livres que vous pouvez emprunter : \n {biblio.books_list}" )
                            new_borrow = str(input("Veuillez entrer la référence du livre que vous voulez emprunter ?\n").lower())
                            connected_user.Borrow(new_borrow)
                            biblio.object_by_ref(new_borrow).noDispo()
                            biblio.object_by_ref(new_borrow).dateBackto()
                            print(f"Vous venez d'emprunter {biblio.object_by_ref(new_borrow)}et il vous faudra le rendre avant la date du {biblio.object_by_ref(new_borrow).dateBackto()}\n Vous avez en votre prossesion les livres suivants : " )
                            for i in connected_user.borrow:
                                print(biblio.object_by_title(i))
                            input()
                            ok = False

                        #Fonctionnalité Prolonger un emprunt
                        elif entry == 2:
                            book_borrow = str(input(f"Voici les livres que vous avez en votre possession :\n {connected_user.borrow}\n Veuillez saisir la référence dont vous voulez prolonger le prêt ?"))
                            addDays = int(input(f"De combien de jour voulez-vous prolonger votre prêt sur ce livre ?\n"))
                            biblio.object_by_ref(book_borrow).extendBorrow(addDays)
                            print(f"Le livre référence {book_borrow} devra dorénavant être rendu le {datetime.date.strftime(biblio.object_by_ref(book_borrow).backto, '%A %d %B %Y')}")
                            ok = False

                        # Fonctionnalité rendre un livre
                        elif entry == 3:
                            book_borrow = str(input(f"Voici les livres que vous avez en votre possession :\n {connected_user.borrow}\n Veuillez saisir la référence que vous voulez rendre ?"))
                            connected_user.BackTo(book_borrow)
                            biblio.object_by_ref(book_borrow).Dispo()
                            biblio.object_by_ref(book_borrow).returnBookDate()
                            print(f"Vous venez de rendre le livre réf.{book_borrow}")
                            ok = False

                        elif entry == 4:
                            changement = True
                            mdp = input("Entrez votre mot de passe actuel\n")
                            compteur  = 0
                            while not verif_user(biblio.users_list, logUser, mdp):
                                compteur += 1
                                print("ok")
                                mdp = input("Entrez encore votre mot de passe actuel\n")
                                if compteur > 2:
                                    changement = False
                                    print("Au revoir !")
                                    break
                            if changement:
                                new_mdp = input("Entrez votre nouveau mot de passe\n")
                                changement_mdp(biblio.users_list, logUser, new_mdp)
                                print("Un instant nous vérifions vos informations ...")
                                print("————————————————————————————————————")
                                time.sleep(1)
                                print("Changement du mot de passe réussi !")
                                print("————————————————————————————————————")
                                ok = False


                        elif entry == 5:
                            infini = False
                            print("Vous êtes déconnectez")
                            inscrire = True

                        elif entry >= 6:
                            print("Veuillez faire un choix présent dans la liste")
                            ok = False


                ###----fin connexion d'un utilisateur----###

        elif entry >= 3:
            print("Veuillez faire un choix présent dans la liste")
            ok = False












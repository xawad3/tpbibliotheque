# from dbm.ndbm import library
from functions import *
from Person_ import *
from Library_ import *
from Users_ import *
import time
import string




choice = ["Rechercher un livre", "Créer un compte", "Se connecter", "J'ai perdu mes identifiants"]
choice1 = ["Rechercher un livre", "Emprunter un livre", "Prolonger un emprunt", "Rendre un livre","Changer votre mot de passe", "Se déconnecter"]
choice2 = ["Par auteur", "Par genre", "Par catégorie", "Par titre", "Par langue", "Revenir au menu précédent"]
sub = ["Je ne veux pas m'abonner","10 Noises/mois (1 livre emprunté par mois)", "5 Mornilles/mois (jusqu'à 2 livres à la fois)", "10 Mornilles/mois (jusqu'à 3 livres à la fois)", "10 Gallions/mois (jusqu'à 4 livres à la fois)"]
biblio = Library("Pourdlard")
biblio.import_books()
biblio.import_user()

# Ajout de livre dans la biblio pour la matière
# user1 = Users("Potter", "Harry", "drago")
# biblio.users_list.append(user1)
# biblio.add_a_book(book1)
# biblio.add_a_book(book2)
# biblio.add_a_book(book3)
# biblio.add_a_book(book4)
# biblio.add_a_book(book5)
# biblio.add_a_book(book6)
# biblio.add_a_book(book7)
# biblio.add_a_book(book8)
# biblio.add_a_book(book9)
# biblio.add_a_book(book10)
# biblio.add_a_book(book12)
#
# print(user1)


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

            elif choix ==4:
                biblio.books_by_language(input("Ecrivez la langue du livre\n"))
            else:
                ok = False

        elif entry == 1:
            name = input("Quel est votre nom ?\n")
            first_name = input("Quel est votre prénom ?\n")
            pwd = input("Choisissez un mot de passe: \n")
            mail = input("Entrez votre adresse mail\n")
            #test = longeurmdp(pwd)
            while not longeurmdp(pwd):

                pwd = input("Votre mot de passe doit faire au moins 5 caractères veuillez retaper un mot de passe correct.\n")

            print("Un instant nous vérifions vos informations ...")
            print("————————————————————————————————————")
            time.sleep(1)
            new = Users(name, first_name, pwd, mail)
            print("Félicitations votre compte utilisateur a été créé, voici votre identifiant", new.id, "prenez soin de le noter !")
            print("————————————————————————————————————")
            biblio.users_list.append(new)

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
            time.sleep(0.5)
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
                inscrire = True
                ok = False

            if connexion:
                for users in biblio.users_list:
                    if logUser.lower() == users.id.lower():
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
                            #début abonnement d'un utilisateur
                            abo = True
                            while abo:
                                if connected_user.rank == 0: #on vérifie que l'utilisateur est abonné
                                    print("Vous devez être abonné(e) pour emprunter un livre !")
                                    Menu(sub)
                                    entry2 = int(input("Choisissez le montant de votre abonnement"))

                                    if entry2 == 0:
                                        print("C'est dommage !")
                                        abo = False
                                        borrows = False
                                        ok = False

                                    elif entry2 == 1:
                                        connected_user.rank = 1
                                        print("———————————")
                                        print("Merci pour votre abonnement votre rang est désormais de 1 !\n" 
                                              "Vous pouvez emprunter un livre à la fois !")
                                        print("———————————")
                                        abo = False
                                        borrows = True

                                    elif entry2 == 2:
                                        connected_user.rank = 2
                                        print("———————————")
                                        print("Merci pour votre abonnement votre rang est désormais de 2 !\n" 
                                              "Vous pouvez emprunter jusqu'à deux livres en même temps !")
                                        print("———————————")
                                        abo = False
                                        borrows = True

                                    elif entry2 == 3:
                                        connected_user.rank = 3
                                        print("———————————")
                                        print("Merci pour votre abonnement votre rang est désormais de 3 !\n"
                                        "Vous pouvez emprunter jusqu'à trois livres en même temps !")
                                        print("———————————")
                                        abo = False
                                        borrows = True

                                    elif entry2 == 4:
                                        connected_user.rank = 4
                                        print("———————————")
                                        print("Merci pour votre abonnement votre rang est désormais de 4 !\n"
                                              "Vous pouvez emprunter jusqu'à quatre livres en même temps !")
                                        print("———————————")
                                        abo = False
                                        borrows = True
                                else:
                                    borrows = True

                                # fonctionnalité emprunter un livre
                                while borrows:
                                    emprunt = len(connected_user.borrow)
                                    if emprunt == connected_user.rank:
                                        print("Vous avez atteint votre maximum d'emprunt ! Ramenez nous des livres pour pouvoir continuer à emprunter !")
                                        borrows = False
                                        abo = False
                                        ok = False
                                    else:
                                        print("Voici la liste des livres que vous pouvez emprunter :")
                                        biblio.mybooks()
                                        new_borrow = str(input("Veuillez entrer la référence du livre que vous voulez emprunter ?\n").lower())
                                        connected_user.Borrow(new_borrow)
                                        biblio.object_by_ref(new_borrow).noDispo()
                                        print(f"Vous venez d'emprunter le livre dont la référence est {new_borrow} et il vous faudra le rendre avant la date du {biblio.object_by_ref(new_borrow).dateBackto()}\n Vous avez en votre prossesion les livres suivants : {connected_user.borrow}" )
                                        borrows = False
                                        abo = False
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
                            print(f"Vous venez de rendre le livre réf.{book_borrow}, il vous reste {connected_user.borrow} en votre possession.")
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
                                time.sleep(0.5)
                                print("Changement du mot de passe réussi !")
                                print("————————————————————————————————————")
                                ok = False


                        elif entry == 5:
                            infini = False

                            print("Vous êtes déconnectez")
                            biblio.export_books()
                            biblio.export_users()
                            inscrire = True
                            break
                        elif entry >= 6:
                            print("Veuillez faire un choix présent dans la liste")
                            ok = False


                ###----fin connexion d'un utilisateur----###

        elif entry == 3:
            id = False
            name = input("Veuillez entrer votre nom")
            first = input("Veuillez entrer votre prénom")
            mail = input("Veuillez entrer votre mail")
            while perte_id(biblio.users_list, name, first, mail):
                new_id = name[0] + "." + first
                new_pwd = random_pwd(5)
                changement_mdp(biblio.users_list, new_id, new_pwd)
                print("Votre id est", new_id)
                print("Votre nouveau mot de passe est", new_pwd, "prenez soin de le noter")
                id = False
                biblio.export_users()
                inscrire = True
                ok = False
                break

            else:
                print("Vous vous êtes trompé !")
                id = False





        elif entry == 4:
            inscrire = False
            ok = False

        elif entry > 4:
            print("Veuillez faire un choix présent dans la liste")
            ok = False














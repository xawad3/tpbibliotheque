# from dbm.ndbm import library
from functions import *
from Person_ import *
from Library_ import *
from Users_ import *
import time
import string



####----MENU UTILISATEUR NON CONNECTÉ----####
choice = ["Rechercher un livre", "Créer un compte", "Se connecter", "J'ai perdu mes identifiants", "Quitter le programme"]

####----MENU UTILISATEUR CONNECTÉ----####
choice1 = ["Rechercher un livre", "Emprunter un livre", "Prolonger un emprunt", "Rendre un livre","Changer votre mot de passe", "Se déconnecter"]

####----MENU RECHERCHE D'UN LIVRE----####
choice2 = ["Par auteur", "Par genre", "Par catégorie", "Par titre", "Par langue", "Revenir au menu précédent"]

####----MENU DES ABONNEMENTS----####
sub = ["Je ne veux pas m'abonner","10 Noises/mois (1 livre emprunté par mois)", "5 Mornilles/mois (jusqu'à 2 livres à la fois)", "10 Mornilles/mois (jusqu'à 3 livres à la fois)", "10 Gallions/mois (jusqu'à 4 livres à la fois)"]

####----CREATION DE LA BIBLIOTHEQUE----####
biblio = Library("POUDLARD")
biblio.import_books() ##--importation des livres dans la bibliothèque
biblio.import_user() ##--exportation des livres dans la bibliothèque



# Ajout de livre dans la biblio pour la matière
# user1 = Users("Potter", "Harry", "drago")
# biblio.users_list.append(user1)
# biblio.add_a_book(bd1)
# biblio.add_a_book(bd2)
# biblio.add_a_book(book13)
# biblio.add_a_book(book14)
# biblio.add_a_book(book15)
# biblio.add_a_book(book20)
# biblio.add_a_book(book21)
# biblio.add_a_book(book22)
# biblio.add_a_book(book23)
# biblio.add_a_book(book24)
# biblio.add_a_book(book25)
# biblio.add_a_book(book26)
# biblio.add_a_book(book27)
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
        ###----DEBUT ENREGRISTREMENT D'UN UTILISATEUR----###
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
            ##test = longeurmdp(pwd)##
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
        ###----FIN D'ENREGISTREMENT UTILISATEUR----##



        ###----DEBUT TENTATIVE CONNEXTION D'UN USER----###
        elif entry == 2:
            inscrire = False
            connexion = True
            logUser = input("Veuillez entrer votre log-in\n")
            psdUser = input("Veuillez entrer votre mdp\n")
            print("Un instant nous vérifions vos informations ...")
            print("————————————————————————————————————")
            time.sleep(0.5)
        ###-----DEBUT VERIFICATION ID ET DU MDP----#
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
        ###----au bout de trois essais, on break le programme----#


            if connexion:
                for users in biblio.users_list:
                    if logUser.lower() == users.id.lower():
                        connected_user = users #--on enregistre l'user connecté pour pouvoir le ré-utiliser--#
                print("Connexion réussie")
                print("————————————————————————————————————")

        ####----DEBUT CONNEXION D'UN USER----###

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




                        ####----FONCTIONNALITE EMPRUNTER UN LIVRE----####
                        elif entry == 1:
                            ####----DEBUT ABONNEMENT USER----####
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

                                borrows = True
                                # fonctionnalité emprunter un livre
                                while borrows:
                                    emprunt = len(connected_user.borrow)
                                    if emprunt == connected_user.rank:
                                        print("Vous avez atteint votre maximum d'emprunt ! Ramenez nous des livres pour pouvoir continuer à emprunter !")
                                        print("Vous pouvez souscrire à un nouvel emprunt !")
                                        borrows = False
                                        abo = False
                                        ok = False
                                        newabo = True
                                        while newabo:
                                            Menu(sub)
                                            entry3 = int(input("Choisissez un nouvel abonnement !"))
                                            if entry3 == 0:
                                                print("dommage")
                                                abo = False
                                                borrows = False
                                                ok = False
                                                newabo = False

                                            elif entry3 == 1:
                                                connected_user.rank = 1
                                                print("———————————")
                                                print("Merci pour votre abonnement votre rang est désormais de 1 !\n"
                                                      "Vous pouvez emprunter un livre à la fois !")
                                                print("———————————")
                                                newabo = False
                                                borrows = True

                                            elif entry3 == 2:
                                                connected_user.rank = 2
                                                print("———————————")
                                                print("Merci pour votre abonnement votre rang est désormais de 2 !\n"
                                                      "Vous pouvez emprunter jusqu'à deux livres en même temps !")
                                                print("———————————")
                                                newabo = False
                                                borrows = True

                                            elif entry3 == 3:
                                                connected_user.rank = 3
                                                print("———————————")
                                                print("Merci pour votre abonnement votre rang est désormais de 1 !\n"
                                                      "Vous pouvez emprunter jusqu'à trois livres à la fois !")
                                                print("———————————")
                                                newabo = False
                                                borrows = True

                                            elif entry3 == 4:
                                                connected_user.rank = 4
                                                print("———————————")
                                                print("Merci pour votre abonnement votre rang est désormais de 1 !\n"
                                                      "Vous pouvez emprunter quatre livres à la fois !")
                                                print("———————————")
                                                newabo = False
                                                borrows = True


                                        
                                    else:
                                        try :
                                            print("Voici la liste des livres que vous pouvez emprunter :")
                                            biblio.mybooks()
                                            new_borrow = str(input("Veuillez entrer la référence du livre que vous voulez emprunter ?\n").lower())
                                            if biblio.object_by_dispo(new_borrow) == False:
                                                print("--------------------------------------------")
                                                print("Ce livre n'est pas disponible pour le moment")
                                                print("--------------------------------------------")
                                                input("Appuyer sur une touche pour continuer")
                                                borrows = False

                                            else:
                                                connected_user.Borrow(new_borrow)
                                                biblio.object_by_ref(new_borrow).noDispo()
                                                biblio.object_by_ref(new_borrow).dateBackto()
                                                print("--------------------------------------------")
                                                print(f"Vous venez d'emprunter {biblio.object_by_ref(new_borrow)}et il vous faudra donc le rendre avant la date du {biblio.object_by_ref(new_borrow).dateBackto()}")
                                                print("--------------------------------------------")
                                                print ("Vous avez en votre prossesion les livres suivants : ")
                                                print("--------------------------------------------")
                                                for i in connected_user.borrow:
                                                    print(biblio.object_by_title(i))

                                                input("Veuillez appuyer sur une touche pour continuer...")
                                                borrows = False
                                                abo = False
                                                ok = False
                                        except AttributeError :
                                            connected_user.BackTo(new_borrow)
                                            print("--------------------------------------------")
                                            print("Cette référence n'existe pas dans notre bibliothèque")
                                            print("--------------------------------------------")
                                            input("Appuyer sur une touche pour continuer")


                        #Fonctionnalité Prolonger un emprunt
                        elif entry == 2:
                            if len(connected_user.borrow) == 0:
                                print("Vous n'avez aucun livre en votre possession !\n")
                                ok = False
                            else :
                                print("Vous avez en votre prossesion les livres suivants : ")
                                print("--------------------------------------------")
                                for i in connected_user.borrow:
                                    print(biblio.object_by_title(i))
                                book_borrow = str(input(f"Veuillez saisir la référence dont vous voulez prolonger le prêt ?\n"))
                                for i in connected_user.borrow:
                                    if i == book_borrow :
                                        addDays = int(input(f"De combien de jour voulez-vous prolonger votre prêt sur ce livre ?\n"))
                                        biblio.object_by_ref(book_borrow).extendBorrow(addDays)

                                        print(f"Le livre référence {book_borrow} devra dorénavant être rendu le {datetime.date.strftime(biblio.object_by_ref(book_borrow).backto, '%A %d %B %Y')}")
                                        ok = False
                                else :
                                    print("Vous n'avez pas emprunter ce livre !")
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














##---fontion pour la création d'un menu---##

def Menu(a): #on rentre en paramètre une liste de choix
    for i in range(len(a)):
        print(f"{i}: {a[i]}") #on affiche les choix présents dans la liste et leur index respectif.


##---fontion pour vérifier la laongueur du mdp---##

def longeurmdp(mdp): #on rentre en paramètre un mdp
    if len(mdp) < 5: #on choisi la longueur minimum du mdp
        return False
    else:
        return True #on se sert d'un bouléen pour vérifier si la lonfueur est bonne.


##---fontion pour la vérification de l'existence de l'user et son mdp---##

def verif_user(liste_u, log, pwd): #on rentre en paramètre la liste des users, l'id et le mdp
    for i in liste_u:
        if log.lower() == i.id.lower():
            if pwd == i.pwd:
                return True
    return False

def verif_author(biblio, liste_a, author):
    for i in liste_a:
        if author.lower() in i.liste_a.lower():
            biblio.books_by_author(input("Ecrivez le nom de l'auteur\n"))
        else:
            print("Nous ne trouvons pas votre recherche")


##---fontion pour le changement du mdp---##

def changement_mdp(liste_u, log, pwd): #on rentre en paramètre la liste des users, l'id et le mdp
    for i in liste_u:
        if log == i.id: #on vérifie que l'id de l'user est le bon et on change son mdp
            i.pwd = pwd


def perte_id(liste_u, name, firstname, mail):
    for i in liste_u:
        if name == i.name_user:
            if firstname == i.first_name_user:
                if mail == i.mail:
                    return True
        else:
            return False



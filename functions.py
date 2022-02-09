
def Menu(a):
    for i in range(len(a)):
        print(f"{i} : {a[i]}")

def longeurmdp(mdp):
    if len(mdp) < 5:
        return False
    else:
        return True

def verif_user(liste_u, log, pwd):
    for i in liste_u:
        if log == i.id:
            if pwd == i.pwd:
                return True
    return False


def changement_mdp(liste_u, log, pwd):
    for i in liste_u:
        if log == i.id:
            i.pwd = pwd



class Person:
    def __init__(self, name_user, first_name_user, pwd, mail):
        self.name_user = name_user
        self.first_name_user = first_name_user
        self.pwd = pwd
        self.mail = mail
        self.id = name_user[0] + "." + first_name_user

    def getMyName(self):
        return self.name_user


    def __repr__(self):
        affiche = f"{self.name_user} {self.first_name_user} son identifiant est {self.id}"
        return affiche




#user = Person("Harry", "Potter", "hezroheogh")
#user1 = Person("HARRY", "P", "djdjdjdj")
#print(user)
#print(user1)

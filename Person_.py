
class Person:
    def __init__(self, name, firstName, pwd):
        self.name = name
        self.firstName = firstName
        self.pwd = pwd
        self.id = name[0] + "." + firstName

    def __repr__(self):
        affiche = f"{self.name} {self.firstName} son identifiant est {self.id}"
        return affiche




#user = Person("Harry", "Potter", "hezroheogh")
#user1 = Person("HARRY", "P", "djdjdjdj")
#print(user)
#print(user1)

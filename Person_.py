
class Person:
    def __init__(self, name, firstName, pwd):
        self.name = name
        self.firstName = firstName
        self.pwd = pwd
        self.id = name[0] + "." + firstName

    def __repr__(self):
        affiche = f"{self.name} {self.firstName} {self.id}"
        return affiche



user = Person("Harry", "Potter", "hezroheogh")
print(user)
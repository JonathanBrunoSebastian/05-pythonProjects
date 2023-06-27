# Object Orientated Programming in Python

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        
    def get_name(self):
        return print(self.name) 

    def get_age(self):
        return print(self.age)

    def set_age(self, age):
        self.age = age

bill = Dog("Bill", 6)
soren =  Dog("Soren", 16)
bill.set_age(17)
bill.get_name()
bill.get_age()
soren.get_name()
soren.get_age()

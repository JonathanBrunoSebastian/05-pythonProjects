# Object Orientated Programming in Python

class Person:
    number_of_people = 0
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

    def show(self):
        print(f"I am {self.name}.")

p1 = Person("Tim")
p2 = Person("Paula")
p3 = Person("Julia")
Person.add_person()
Person.add_person()
print(Person.number_of_people_())
p3.show()

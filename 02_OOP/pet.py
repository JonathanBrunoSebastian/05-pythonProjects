# Object Orientated Programming in Python

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and my age is {self.age} years.")

    def speak(self):
        print("I don't know what to say.")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meaw")

    def show(self):
        print(f"I am {self.name}, my age is {self.age} years and I am {self.color}.")

class Dog(Pet):
    def speak(self):
        print("Wow")

class Fish(Pet):
    pass            # speak not defined

p = Pet("Tim", 21)
p.show()
c = Cat("Lissa", 6, "yellow")
c.show()
c.speak()
d = Dog("Bernd", 43)
d.show()
d.speak()
f = Fish("Lolup", 24)
f.show()
f.speak()

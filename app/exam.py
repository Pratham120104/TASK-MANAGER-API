class Dog:
    species = "canine"

    def __init__(self, name, age):
        self.name = name
        self.age = age


dog1 = Dog("Max", 5)
print(dog1.name)
print(dog1.species)

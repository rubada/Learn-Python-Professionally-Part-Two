# The 4 Pillars of OOP in Python:
# 2. Polymorphism
# "Polymorphism" means "many forms", and in programming when a methods,
# or functions, etc., have the same name and can be executed on many objects of
# the different or same type.
# Let's take an example:
# The len() function, can be executed on different data types:
# Lists
# print(len([2, 5, 3, 1]))

# Strings
# print(len("Hello"))

# Dictionary
# print(len({"g": 1, "h": 2, "y": 4, "u": 5, "N": 7}))


# Class Polymorphism
# Polymorphism is used with class methods, where there is a method that has
# the same name in multiple classes.
# Let's take an example:
class Dogs:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        return "Heard my dog barking."


class Cats:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        return "Heard my cat meowing."


class Roosters:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        return "Heard my rooster crowing."


# Create classes instances:
dog = Dogs("leo", 6)
cat = Cats("Oreo", 2)
rooster = Roosters("RuRu", 1)

# To call the sound method for all the objects, we the "for" loop:
# for i in [dog, cat, rooster]:
#     print(i.sound())

# Because of Polymorphism we can excute the sound() method for the three
# classes.


# Polymorphism with Inheritance:
class Animals:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        return f"{self.name} voice"


class Dog(Animals):

    # Reuse and override the sound method in the Animals class in the Dog
    # subclass
    def sound(self):
        return f"{super().sound()} is barking."


class Cat(Animals):

    # Override the sound method in the Animal class and inherit the Animal
    # attributes.
    def sound(self):
        return f"{self.name} is meowing."


class Rooster(Animals):

    # Override the sound method in the Animal class and inherit the Animal
    # attributes.
    def sound(self):
        return f"{self.name} is crowing."


dog = Dog("leo", 6)
cat = Cat("Oreo", 2)
rooster = Rooster("RuRu", 1)
names = ["dog", "cat", "rooster"]
animals_obj = [dog, cat, rooster]

for i in range(len(names)):
    print(f"My {names[i]} {animals_obj[i].name} age is {animals_obj[i].age} \
years old")
    print(animals_obj[i].sound())

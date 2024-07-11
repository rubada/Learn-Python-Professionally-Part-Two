# The 4 Pillars of OOP in Python:
# 3. Encapsulation
# Encapsulation is wrapping the data (attributes) and the methods into one
# single unit, known as the class.
# This will control access to some data components and methods, prevent them
# from direct access or modification (outside the class), and allow only the
# methods inside to access and modify these data and methods.
# This will lead us to the three types of data members.
# There are three types of data (attributes and methods) can be defined inside
# the class:
# 1. Public Members, which are the attributes and methods that can be accessed
# and modified directly, when creating an instance from the class.

class Dogs:
    # Public attribute
    brand = "Husky"

    def __init__(self, name, age):
        # Public attribute
        self.name = name
        self.age = age

    # Public method
    def bark(self):
        print("Uf Uf")


dog_obj = Dogs("Leo", 6)
# print(dog_obj.name)
# print(dog_obj.age)
# print(dog_obj.brand)
# print(dog_obj.bark())
dog_name = dog_obj.__dict__["name"] = "Silver"
# print(dog_obj.name)


# 2. Protected Members are only accessible inside the class itself, and also
# can be accessed by the subclasses.
# Protected Members' names should start with a single underscore "_"
# Although the protected members can be accessed and modified out of the
# class, programmers should refrain from accessing and modifying them
# outside the class body.

class DogsRev:

    def __init__(self):
        # Protected Attribute
        self._name = "Leo"
        self._age = 6

    # Protected Method
    def _sound_age(self):
        return f"{self._name} is barking, his age is {self._age}"

    # Using the protected method inside another method
    def dog_property(self):
        return self._sound_age()


class Dog(DogsRev):
    brand = "Husky"

    def dog_brand(self):
        return f"My dog {self._name} is a {Dog.brand}"


dog_obj1 = Dog()
# print(dog_obj1._name)
# print(dog_obj1._sound_age())
# Can be accessed outside the class and used by subclasses,
# but they shouldn't.
# print(dog_obj1.dog_brand())
# print(dog_obj1.dog_property())


# 3. Private Members are members of the class, they can't be used, accessed,
# or modified inside the subclasses, and can't be modified or accessed outside
# the class, they can be only used inside the superclass or the class they are
# defined in.
# To define these private members use double underscores "__" before their
# names.

class DogsRev1:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Private Attribute
        self.__bark = "barking"

    # Private Method
    def __sound_age(self):
        return f"{self.name} is {self.__bark}, his age is {self.age}"

    def dog_property(self):
        return self.__sound_age()


class DogOne(DogsRev1):

    def sound(self):
        return super().__sound_age()

    def bark(self):
        return super().__bark


dogs_parent = DogsRev1("Blade", 3)
# print(dogs_parent.__bark)
# print(dogs_parent.__sound_age())
# print(dogs_parent.dog_property())

dogs_child = DogOne("Blade", 3)
# print(dogs_child.__bark)
# print(dogs_child.sound())
# print(dogs_child.bark())
# print(dogs_child.dog_property())


# Thus Encapsulation emphasizes data hiding and controls how to access and
# modify the class attributes and methods.

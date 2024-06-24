# The 4 Pillars of OOP in Python:
# 1. Inheritance
# Inheritance is inheriting all of a class's methods and properties to another
# class.
# In inheritance, there are two classes:
# 1. Parent class is the class that it is inherited from, also called base
# class.
# 2. Child class is the class inherited from the parent class, also called
# derived class.
# Let's take an example:


# 3. Multilevel inheritance:
class Parent:
    x = 3


class Child1(Parent):
    y = 45


class Child2(Parent):
    z = 60


class GrandChild(Child1, Child2):
    pass


# GrandChild inherits from Child1, Child2, and Parent.
num1 = GrandChild()
# print(num1.x)
# print(num1.y)
# print(num1.z)

# Beware when using multilevel inheritance, because it can complicate the code
# and make it difficult to understand.


# The benefits of inheritance are:
# 1. Reusability, when a class inherits another class, the child class can
# access all the functionality of the parent class.
# 2. Reusability makes our code reliable because the base or parent class is
# already tested and debugged.
# Example:
class ListChild(list):
    pass

# Using the built-in list class as the parent class that is already tested and
# debugged.

# 3. Reuse the parent class will lead to low development time and maintenance
# cost, and D.R.Y, prevent code repetition.

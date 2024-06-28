# What is a Method Resolution Order (MRO)?
# MRO is the classes (Superclasses, subclasses) order that Python searches for
# attributes or methods.
# First Python searches for the methods or attributes in the class itself, then
# it follows the order of inheritance.
# Let's take an example:
class Parent:

    def who_I_am(self):
        return "I am the Parent"


class Child1(Parent):

    def who_I_am(self):
        return "I am Child1"


class Child2(Parent):

    def who_I_am(self):
        return "I am Child2"


class GrandChild(Child1, Child2):

    def who_I_am(self):
        return "I am the GrandChild"


# To get the MRO we use the mro() method:
# print(GrandChild.mro())

# That means if I want to execute the who_I_am(), if the object is created
# from the GrandChild class, then Python will search the Grandchild class
# first.

grand_child = GrandChild()
# print(grand_child.who_I_am())

# That's why we should be extra careful when using multi-level inheritance,
# because it may lead to undesirable results.

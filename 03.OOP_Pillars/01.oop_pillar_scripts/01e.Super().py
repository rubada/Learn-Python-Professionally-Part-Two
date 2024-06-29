# Super()
# Using super() in Python has several advantages over using the parent class
# name:
# 1. "super()" make your code maintainable, which means if you decide to change
# the parent class name or the inheritance hierarchy, by using super() there is
# there is no need to change the class name in all the subclasses (children
# classes).
# 2. Using "super()" in multi-level inheritance is convenient if you understand
# the MRO of your classes.

# Let's take an example, showing the result if the classes have inside them a
# method with the same name:

class Parent:

    def who_I_am(self):
        return "I am the Parent"


class Child1(Parent):

    def who_I_am(self):
        print(f"{super().who_I_am()}, inside Child1")
        return "I am Child1"


class Child2(Parent):

    def who_I_am(self):
        print(f"{super().who_I_am()}, inside Child2")
        return "I am Child2"


class GrandChild(Child1, Child2):

    def who_I_am(self):
        print(f"{super().who_I_am()}, inside GrandChild")
        return "I am the GrandChild"


# print(GrandChild.mro())

grand_child = GrandChild()
# print(grand_child.who_I_am())


# Let's take an example with different methods names for "Child2" class and
# "GrandChild" class:
class Parent:

    def who_I_am(self):
        return "I am the Parent"


class Child1(Parent):

    def who_I_am_one(self):
        print(f"{super().who_I_am()}, inside Child1")
        return "I am Child1"


class Child2(Parent):

    def who_I_am_two(self):
        print(f"{super().who_I_am()}, inside Child2")
        return "I am Child2"


class GrandChild(Child1, Child2):

    def who_I_am_three(self):
        print(f"{super().who_I_am_one()}, inside GrandChild")
        return "I am the GrandChild"


# print(GrandChild.mro())

grand_child = GrandChild()
# print(grand_child.who_I_am_three())


# "super()" is a powerful tool if it is used correctly and carefully, but be
# carful when using it in mutli-level inheritance, because it may complicate
# your code and you may get undesirable results.

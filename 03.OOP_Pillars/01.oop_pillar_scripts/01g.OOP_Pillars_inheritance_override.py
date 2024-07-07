# Methods Override.
# An override allows a subclass (child) method to provide its implementation
# over a method (that has the same name) that is already defined in its
# superclass (parent).
# Let's take an example:
class Parent:

    def to_overide(self):
        return "This method is inside the Parent class"


class Child(Parent):

    def to_overide(self):
        return "This method is inside the Child class"


# Create an instance of the Child class
object_sub = Child()
# print(object_sub.to_overide())


# Overriding can be used in:
# 1.Multiple Inheritance
class Parent1:

    def to_overide(self):
        return "This method is inside the Parent1 class"


class Parent2:

    def to_overide(self):
        return "This method is inside the Parent2 class"


class ChildRev(Parent1, Parent2):

    def to_overide(self):
        return "Inside the Child class"


# Create an instance of the Child class
obj_sub = ChildRev()
# print(obj_sub.to_overide())


# 2.Multilevel Inheritance:
class ParentRev:

    def to_overide(self):
        return "Inside the ParentRev class"


class Child1(ParentRev):

    def to_overide(self):
        return "Inside the Child1 class"


class GrandChild(Child1):

    def to_overide(self):
        return "Inside the GrandChild class"


sub_child = Child1()
# print(sub_child.to_overide())

grand_child = GrandChild()
# print(grand_child.to_overide())


# Where and why do we use method overriding?
# 1. Maintainability: When you use method overriding, you can change the
# behavior of methods in a subclass without altering the superclass code.

# 2. Polymorphism.
# Method overriding enables polymorphism, allowing different objects to respond
# differently to the same method call. Different versions of the methods are
# called based on the object type.
# Polymorphism will be discussed in the next section.

# 3. Overriding is used in abstraction, which will be discussed later in this
# section.

# 4. The above points lead to code flexibility.

# The 4 Pillars of OOP in Python:
# 4. Abstraction:
# Let us take an example of a real-world scenario when you use the apps on your
# smartphone such as recording a video or audio, sending emails, securing your
# phone by adding a password, pattern, face recognition, etc., you do not know
# how your phone executes these apps, you only touch your phone screen to
# perform these actions.

# Thus abstraction is a concept in Python that hides complex implementation
# details while exposing only essential information and to users.

# How can we create a user-defined abstract class?
# We can create an abstract class by using the "abc" module.
# Let us take an example:

# To create an abstract class, we must import the "ABC" class, and
# abstractmethod from the "abc" module:
from abc import ABC, abstractmethod


# Then defining the abstract class which inherits the ABC class:
class AbstractClass(ABC):

    # Abstract class methods:
    # 1. The abstract method or methods, these methods should be declared and
    # lack implementation.
    @abstractmethod
    def abstract_method(self):
        pass

    # 2. Concrete methods are standard methods, and they have implementations.
    # The concrete methods are used when there are methods in the subclasses
    # that have the same implementation, as D.R.Y (Don't Repeat Yourself), we
    # create a method in the abstract class and then it will be inherited and
    # used in the subclasses.
    # This will enhance code reusability and maintainability (debugging).

    def concrete_method(self):
        return "This is a normal method exists inside the abstract class"

# Create an instance from the abstract class.
# parent = AbstractClass()

# A TypeError will be raised, because we cannot create instances from the
# abstract classes because they cannot be instantiated directly, they are
# abstract (the user doesn't need to know their existence), and the abstract
# classes require subclasses to be instantiated (create instances).


# Now, let's create a subclass that is inherited from the abstract class.
# A class that inherits an abstract class is called a concrete class.
# A subclass of an abstract class can be instantiated only if it overrides all
# the abstract methods in the abstract class.

class SubClassOne(AbstractClass):

    # Create a method that will override the abstract method in the abstract
    # class.
    # A TypeError will be raised if the subclass does not have a method to
    # override the abstract method.
    def abstract_method(self):
        return "This is a method in SubClass number one."

    def normal_method(self):
        return "Normal method of SubClass"


# Creating an instance for SubclassOne()
obj_sub = SubClassOne()
print(obj_sub.abstract_method())

# Invoke the concrete method
# print(obj_sub.concrete_method())

# print(obj_sub.normal_method())

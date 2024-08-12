# "staticmethod()" Function:
# It is a method that belongs to the class, and it is not related to the class
# instances, it can't change the class state or the instance state.
# It can be used to perform operations that do not require access to the class
# variables or creating class instance.
# Syntax:
# staticmethod(function)
# Parameter:
# function: The staticmethod accepts a function (method) and converts it into a
# static method.
# Return:
# A method method for the given function.
# Example:
class MathOperations:

    def addition(a, b, c):
        return a + b + c


# Call the mehtod by creating an instance, an error will be raised, because it
# doesn't have the self parameter, and the attributes are not defined:
add = MathOperations()
# print(add.addition(1, 2, 4))

# To solve the above the staticmethod() is used:
MathOperations.addition = staticmethod(MathOperations.addition)
# print(MathOperations.addition(1, 2, 3))


# Same as classmethod, staticmethod can be used a decorator:
class MathOperations:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def addition(a, b, c):
        return a + b + c


# Calling the static method using the class
addition = MathOperations.addition
# print(addition(3, 4, 7))


# Now  what is the difference between a static method and a class method,
# the class method have the parameter "cls", where it can be used and modified
# inside the class method, while the static method doesn't have the "cls"
# parameter, even it the cls added as a parameter it will not refer to the
# class itself.

class MathOperationsRev:
    x = 2

    @staticmethod
    def addition(a, b, c):
        return a + b + c

    @classmethod
    def subtraction(cls, a, b, c):
        cls.x = 4
        return a - b - c - cls.x


addition = MathOperationsRev.addition
# print(addition(3, 4, 7, 1))

subtraction = MathOperationsRev.subtraction
# print(subtraction(3, 4, 7))

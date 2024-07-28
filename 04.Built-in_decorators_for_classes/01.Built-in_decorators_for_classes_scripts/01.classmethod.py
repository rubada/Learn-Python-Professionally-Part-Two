# "classmethod()" Function:
# Syntax
# classmethed(function)
# Parameter:
# function: The classmethod accepts a function (method) and converts it into a
# class method.
# Return:
# A class method for the given function.
# Beware that we are using a class method not the instance method.
# This means that the class method is related to the class itself, not the
# object or the instance, thus no need to create an object to use this method.
# Example:

class MathOperations:

    def addition(self, a, b, c):
        return a + b + c


# Calling the method using the class directly will raise an error:
# print(MathOperations.addition(3, 4, 7))

# Convert addition() to a class method by calling the class:
MathOperations.addition = classmethod(MathOperations.addition)
# print(MathOperations.addition(3, 4, 7))

# Or calling the class object (instance), but beware that the instance
# attributes should be included when creating the object if they are available:
MathOperations.addition = classmethod(MathOperations().addition)
print(MathOperations.addition(3, 4, 7))

# But either way it is still converted to a class method.


# To use the class with these methods, the "cls" parameter is used.
# It is the same "self", as discussed before the "self" represents the
# instances, while the "cls" represents the class.
class MathOperationsRev:
    a = 4
    b = 5
    c = 2

    def addition(cls):
        return cls.a + cls.b + cls.c


MathOperationsRev.addition = classmethod(MathOperationsRev.addition)
# print(MathOperationsRev.addition())

# If the classmethod function is assigned to a variable, it will raise a:
# TypeError: 'classmethod' object is not callable
# The classmethod() can't be called using (), because it is already called.
# That's why we redefine the method "MathOperationsRev.addition" to be able
# to call it again.
add_rev = classmethod(MathOperationsRev.addition)
# print(add_rev())

add_rev1 = MathOperationsRev.addition
# print(add_rev1())


# Instead of using the classmethod function, we can use the classmethod
# as a decorator, as shown below:
class MathOperationsRev1:
    a = 3
    b = 8
    c = 10

    @classmethod
    def addition(cls):
        return cls.a + cls.b + cls.c


# In this case, the classmethod can be assigned to a variable, because we
# didn't call any function.

add_rev2 = MathOperationsRev1.addition
print(add_rev2())

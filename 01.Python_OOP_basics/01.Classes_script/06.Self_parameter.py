# “self” represents the instance (object) of the class. It is used to access
# the methods and attributes defined inside the class.
# “self” is not a keyword, it is a parameter, and it can be given any other
# name, but using “self” as the name is common across the Python community.
# The "self" parameter must be the first parameter of any method in the class.
# As shown below:

class MathOperations:
    # Here instead of "self" we use "mine", and as shown "mine" is defined as
    # the first parameter.
    def __init__(mine, a, b, c=0):
        mine.a = a
        mine.b = b
        mine.c = c

    def addition(self):
        return self.a + self.b + self.c


# print(MathOperations(1, 2, 3).addition())

# "self" as mentioned above, is used to access the methods and attributes
# defined inside the class in three different ways:
# 1. It is used in the __init__ constructor to update the state of the instance
# in other words, modify the object’s properties.
# As shown in the above __init__.

# 2. It is used in the instance method to read the values of the attributes and
# returns an output after using them in an expression or string, in other words
# executes a task using the object attributes.
# As shown above in the addition method.


# 3. Finally, "self" is used if an instance method is called from another
# instance methods.

class AddSub:

    def __init__(self, a, b, c=0):
        self.a = a
        self.b = b
        self.c = c

    def addition(self):
        return self.a + self.b + self.c

    def subtraction(self):
        return self.addition() - self.b


obj = AddSub(3, 4, 1)
# print(obj.addition())
# print(obj.subtraction())

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

# 1. Single Inheritance
class MathOperations:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def addition(self, e, f):
        return self.a + self.b + self.c + e + f

    def subtraction(self):
        return self.a - self.b - self.c

    def multiplication(self):
        return self.a * self.b * self.c

    def division(self):
        return self.a / self.b


class ApplyMath(MathOperations):

    def __init__(self, x, y, a, b, c):
        # MathOperations.__init__(self, a, b, c=0)
        # Or using the super() function, or the class to get the attributes
        # inide the parent class, super() will be discussed later in details.
        super().__init__(a, b, c)
        self.x = x
        self.y = y

    def add_nums(self):
        # Calling the parent methods inside the child class:
        return super().addition(self.x, self.y)


# Creating an instance
obj_add = ApplyMath(3, 5, 1, 2, 4)
# print(obj_add.add_nums())

# Calling the parent methods, using the instance created from the child class.
# print(obj_add.division())

# Check if obj_add is an instance (object) of the MathOperations
# print(isinstance(obj_add, MathOperations))

# Check if a class (child) is a subclass of another class (parent)
# print(issubclass(ApplyMath, MathOperations))


# Inheriting the attributes:
class MathOperationsRev:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def subtraction(self):
        return self.a - self.b - self.c


class ApplyMathRev(MathOperationsRev):

    def sub_nums(self):
        return super().subtraction()

    def attributes(self):
        return f"a = {self.a}\nb = {self.b}\nc = {self.c}"


obj_sub = ApplyMathRev(3, 5, 1)
# print(obj_sub.sub_nums())
# print(obj_sub.attributes())

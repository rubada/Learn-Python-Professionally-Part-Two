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

# 2. Multiple inheritance:
# Parent class number one:
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


# Parent class number Two:
class EvenOdd:

    def __init__(self, num):
        self.num = num

    def even_odd(self):
        if self.num % 2 == 0:
            return f"{self.num} is an even number"
        else:
            return f"{self.num} is an odd number"


class ApplyMathRev(MathOperations, EvenOdd):

    def __init__(self, x, y, c):
        MathOperations.__init__(self, x, y, c)
        EvenOdd.__init__(self, x)
        self.x = x
        self.y = y

    def add_nums(self):
        # Calling the parent methods inside the child class
        return super().addition(self.x, self.y)


# Creating an instance
obj_add1 = ApplyMathRev(3, 5, 1)
# print(obj_add1.add_nums())

# Calling the second parent methods, using the instance created from the child
# class.
print(obj_add1.even_odd())


# But creating a parent class with more than one Child class, will be a good
# approach to prevent repeating yourself (DRY), as shown below:
class Parent:
    pass


class Child1(Parent):
    pass


class Child2(Parent):
    pass


class Child3(Parent):
    pass

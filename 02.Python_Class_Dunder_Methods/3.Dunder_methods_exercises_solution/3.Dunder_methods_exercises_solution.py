# 1st Question:
# Create a class "Books" to return "True" if both books have the same
# published years:
# book1 = Books("Rise of the Knight", 1955)
# book2 = Books("Different People", 1955)
# print(book1 == book2)
# Output = True

# Solution:
class Books:

    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __eq__(self, other):
        if isinstance(other, Books):
            return self.year == other.year
        else:
            return False

    def __hash__(self):
        return hash((self.title, self.year))


book1 = Books("Rise of the Knight", 1955)
book2 = Books("Different People", 1955)
# print(book1 == book2)


# Explanation: When a class defined immutable objects and has the __eq__()
# method, the __hash__() should be defined inside the class, because if the
# __hash__() was not defined a "TypeError: unhashable type" will be raised
# when calling the hash function on the class objects.
# If the class defined mutable objects and has __eq__(), then there is no need
# to define the __hash__().
# As shown in the example below, every object created from a class has a hash
# number, but when __eq__() is defined, if the __hash__() was not defined then
# the above type error will be raised.
# Check __hash__ in Python docs:
# https://docs.python.org/3/reference/datamodel.html#object.__hash__
# For more information about hash() check the below video:
# Python Hash table & Hash Function or Method.
# https://youtu.be/R8xSkRvN4qA
# Check below example, when the __eq__ exists inside the class and when it is
# not
class Person:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    # def __eq__(self, value: object) -> bool:
    #     pass


person1 = Person((1, 2), (3, 5))
# print(hash(person1))
person2 = Person([2, 3], [4, 6])
# print(hash(person2))


# 2nd Question:
# Change below decorator to a class decorator that accepts arguments:
# def multiply_add(x, y):
#     def inner_deco(func):
#         def wrapper(*args, **kwargs):
#             z = func(*args, **kwargs) * 10 + x + y
#             return z
#         return wrapper
#     return inner_deco


# @multiply_add(2, 3)
# def add(a, b):
#     return a + b


# print(add(1, 2))


# Solution:
class MultiplyAdd:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            z = func(*args, **kwargs) * 10 + self.a + self.b
            return z
        return wrapper


@MultiplyAdd(2, 3)
def add(a, b):
    return a + b


# print(add(1, 2))

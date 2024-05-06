# Dunder or magic methods
# These are special methods that are part of built-in classes and user-defined
# classes, when using the dir() function on a class.
# They are called the dunder methods because these methods have a double
# underscore at the beginning and end of their name (dunder means double
# underscore).

# Using the dir() on the "list" class to get a list of its dunder methods:
# print(dir(list))


# Using the dir() on a user-defined class:
class CheckDunder:
    pass


# print(dir(CheckDunder))


# These methods are initiated when the object or instance is created, that's
# means you can get their result without invoking them, same as __init__
# constructor, that is why they are called magic methods.
# Some of these methods can be invoked using the object, although they are
# initiated when the object is created.


# Example:

class Add:

    def __init__(self, a, b, c=0):
        self.a = a
        self.b = b
        self.c = c
        print("This is init")

    def addition(self):
        return self.a + self.b + self.c


# add_value = Add(1, 2, 3)

# There is no need to call or invoke the init method to get a result:
# print(add_value.a)

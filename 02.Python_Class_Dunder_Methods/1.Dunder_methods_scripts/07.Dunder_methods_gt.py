# Examples of dunder methods
# Here we will discuss the most used dunder methods.
# As discussed before dunder methods are invoked or called when the object is
# initiated.
# The below link shows all the dunder methods in Python docs, or you can check
# any other site you prefer:
# https://docs.python.org/3/reference/datamodel.html#special-method-names

# 8. object.__gt__(self, other), greater than which is one of the rich
# comparison methods.
# https://docs.python.org/3/reference/datamodel.html#object.__gt__
class GreaterThan:

    def __init__(self, x):
        self.x = x

    def __gt__(self, other):
        if self.x > other.x:
            return True
        else:
            return False


# Using __gt__ with two objects of the same class:
obj_gt1 = GreaterThan(5)
obj_gt2 = GreaterThan(6)
# print(obj_gt1 > obj_gt2)
# print(obj_gt2 > obj_gt1)


# Using multiple classes
class GreaterThanRev:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __gt__(self, other):
        if self.x > other.x or self.y > other.y:
            return True
        else:
            return False


class AttrClass:

    def __init__(self, x, y):
        self.x = x
        self.y = y


# Using __gt__ with two objects of two different classes
obj_gt1_1 = GreaterThanRev(5, 7)
obj_gt1_2 = AttrClass(6, 3)
# print(obj_gt1_1 > obj_gt1_2)

# Beware when creating two objects of different classes, to put the class that
# has the __gt__ method first:
# print(obj_gt1_2 > obj_gt1_1)

# Another important note, when creating objects of different classes, the
# attributes in both classes should have the same names.

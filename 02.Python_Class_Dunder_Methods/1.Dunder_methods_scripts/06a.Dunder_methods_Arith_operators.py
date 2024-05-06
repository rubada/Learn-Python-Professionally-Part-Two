# Examples of dunder methods
# Here we will discuss the most used dunder methods.
# As discussed before dunder methods are invoked or called when the object is
# initiated.
# The below link shows all the dunder methods in Python docs, or you can check
# any other site you prefer:
# https://docs.python.org/3/reference/datamodel.html#special-method-names

# 7. Arithmetic Operations methods
# https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types
# There are many arithmetic operations, we will talk about two of them the
# __add__, the other arithmetic operations have the same
# implementation:

class AddClass:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # The other refers to the other object (instance), you can name "other"
    # with any name you want.
    def __add__(self, other):
        return self.num1 + self.num2 + other.num1 + other.num2


# Adding two objects of the same class
obj_add1 = AddClass(4, 6)
obj_add2 = AddClass(2, 1)
obj_add3 = obj_add1 + obj_add2
# print(obj_add3)
obj_add4 = obj_add2 + obj_add1
# print(obj_add4)


class AttrClass:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


# Adding two objects of different classes
obj_add1_1 = AddClass(4, 6)
obj_add1_2 = AttrClass(2, 3)
obj_add1_3 = obj_add1_1 + obj_add1_2
# print(obj_add1_3)

# Beware when adding two objects of different classes, to put the class that
# has the __add__ method first:
# obj_add1_4 = obj_add1_2 + obj_add1_1
# print(obj_add1_4)


# __add__ can return the object it self:
class AddClassRev:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other):
        return AddClassRev(self.num1 + other.num1, self.num2 + other.num2)


add1_rev = AddClassRev(4, 3)
add2_rev = AddClassRev(2, 5)
add3_rev = add1_rev + add2_rev
# print(add3_rev)
print(add3_rev.num1)
print(add3_rev.num2)

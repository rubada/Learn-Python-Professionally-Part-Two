# How to get the attributes from a class or object?
# There are two ways to get the class or object attributes and the return
# will be a dictionary:
# 1. Using the __dict__ attribute, it will return a dictionary containing the
# object's attributes, by mapping the attributes' names to their values.
# While using it with the class itself it will return everything related to
# this class as a dictionary.
# 2. Using the vars() function, the argument of the vars function is the
# object or the class, return the same dictionary as __dict__ for a class or
# an object.

class MathOperations:
    # class attributes (class variable2s)
    x = 4
    y = 5
    z = 6

    # instance attributes or variables, __init__ constructor
    def __init__(self, a, b, c=0):
        self.a = a
        self.b = b
        self.c = c

    # methods
    def addition(self):
        return self.a + self.b + self.c + self.x

    def subtraction(self):
        return self.a - self.b - self.c - self.y

    def multiplication(self):
        return self.a * self.b * self.c * self.z

    def division(self):
        return self.a / self.b


# 1. Object1
math_op_obj1 = MathOperations(2, 3, 5)
obj1_dict_attributes = math_op_obj1.__dict__
# print("Using __dict__:")
# print(obj1_dict_attributes)

# Adding new attribute
# obj1_dict_attributes["d"] = 8
# print(obj1_dict_attributes)

print("Using vars():")
# print(vars(math_op_obj1))

# 2. Object2
math_op_obj2 = MathOperations(1, 2)
obj2_dict_attributes = math_op_obj2.__dict__
# print("Using __dict__:")
# print(obj2_dict_attributes)

# Adding new attribute
# obj2_dict_attributes["d"] = 7
# print(obj2_dict_attributes)

# print("Using vars():")
# print(vars(math_op_obj2))


# When using __dict__ on the class itself, it will return all the
# class attributes and methods mapping them to their objects or values.
class_attrib = MathOperations.__dict__
# print(class_attrib)
# print(vars(MathOperations))
# print(class_attrib["addition"])
# print(class_attrib["x"])

# Another example
# print(list.__dict__)

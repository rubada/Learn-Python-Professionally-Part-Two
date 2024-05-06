# Examples of dunder methods
# Here we will discuss the most used dunder methods.
# As discussed before dunder methods are initiated when the object is called.
# The below link shows all the dunder methods in Python docs, or you can check
# any other site you prefer:
# https://docs.python.org/3/reference/datamodel.html#special-method-names

# 1. object.__init__(self[, ...]) dunder method, which is the most used method:
# https://docs.python.org/3/reference/datamodel.html#object.__init__

class Add:

    def __init__(self, a, b, c=0):
        self.a = a
        self.b = b
        self.c = c
        return ("This is init")

    def addition(self):
        return self.a + self.b + self.c


# add_value = Add(1, 2, 3)


# 2. object.__repr__ (self) returns a formal string representation of an
# object, which means an expression that can be executed, as shown below:
# https://docs.python.org/3/reference/datamodel.html#object.__repr__
class DundClass:

    def __init__(self, a, b, c=0):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return f"DundClass({self.a}, {self.b}, c={self.c})"


# Creating an object
add_obj = DundClass(2, 3, 4)

# __repr__ is used in foraml object representation:
# print(add_obj)

# We can use the eval() function with the repr() function, to evaluate the
# object:
add_obj1 = eval(repr(add_obj))
# print(add_obj1.a)

# Two different objects:
print(id(add_obj))
print(id(add_obj1))


# 3. object.__str__(self) is the informal representation of an object, which
# means the returned string is a normal string, not an expression.
# https://docs.python.org/3/reference/datamodel.html#object.__str__
class DundClass1:

    def __init__(self, a, b, c=0):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"This is an instance of class DundClass1 and has the following\
 attributes:\na = {self.a}\nb = {self.b}\nc = {self.c}"


# Creating an object:
add1_obj = DundClass1(2, 3, 4)

# __str__ is used in object informal representation, it can't be evaluated:
print(add1_obj)


# But why this is important, let's discuss it in the next section.

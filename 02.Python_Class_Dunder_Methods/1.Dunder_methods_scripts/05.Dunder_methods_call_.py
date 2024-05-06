# Examples of dunder methods
# Here we will discuss the most used dunder methods.
# As discussed before dunder methods are invoked or called when the object is
# initiated.
# The below link shows all the dunder methods in Python docs, or you can check
# any other site you prefer:
# https://docs.python.org/3/reference/datamodel.html#special-method-names

# 6. object.__call__(self[, args...]), this method is used when the object
# (instance) is required to be called as a function:
# https://docs.python.org/3/reference/datamodel.html#object.__call__
class MainClass:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __call__(self, a, b):
        add_num = a + b + self.num1 + self.num2
        return add_num


obj = MainClass(3, 5)
# print(obj(6, 4))


# The __call__ method can be used when create a class decorator.
# Changing the below decorator to a class decorator:
def multiply_add(func):
    def wrapper(*args, **kwargs):
        x = func(*args, **kwargs) * 10 + 5
        return x
    return wrapper


class MultiplyAdd:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        x = self.func(*args, **kwargs) * 10 + 5
        return x


@MultiplyAdd
def add(a, b):
    return a + b


# print(add(3, 5))

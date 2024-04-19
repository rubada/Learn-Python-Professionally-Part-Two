# Object class:
# What is this the "object" class?
# The object class is the base class for all objects in Python when you define
# a class in Python (even built-in classes), this class will inherit
# the "object" class  automatically, (inheritance will be discussed later in
# this part)


# In Python 3 you can define the class in three different ways:
class ClassName(object):
    pass


class AnotherClass():
    pass


class FinalClass:
    pass

# The above three ways are identical.


# While in Python 2 to inherite the "object" class, the class should be
# defined as follows:
# class ClassName(object):
#     pass

# The user-defined or built-in classes will inherit all the methods that are
# defined in the "object" class.

# print(dir(object))
# print(dir(list))
# print(dir(FinalClass))

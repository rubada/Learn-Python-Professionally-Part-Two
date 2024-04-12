# As discussed before a class is used to create an objects, this is how classes
# are different from functions, the function is used to perform one task, for
# example to perform numbers addition, subtraction, division, multiplication,
# different functions should be written.

# While writing one class will be sufficient to perform the above operations.
# Let's create a simple class that does math operations.
# How are classes defined?
# 1. Use the class keyword then give the class its name, after the name
# parentheses can be used or left without parentheses.
# 4. Create the attributes.
# 3. Create the methods needed. Methods are the behavior of an object, where
# actions can be executed, such as lists dictionaries, etc., methods.
# Methods can be considered functions that belong to a class, they are
# created inside the class, and they are linked to the class or the object
# created from it.
# To invoke or call a method, an object should be created object, then methods
# Can be invoked.
# Methods may have arguments and, the self-argument is required as the
# first argument in a method.

class MathOperations:
    # class attributes (class variables)
    a = 4
    b = 5
    c = 6

    # methods
    def addition(self):
        return self.a + self.b + self.c

    def subtraction(self):
        return self.a - self.b - self.c

    def multiplication(self):
        return self.a * self.b * self.c

    def division(self):
        return self.a / self.b


# This is how a class is created, let's execute this class.
# Note: the self parameter will be discussed later in this section.

# To execute the class follow the below steps:
# 1. Create an object from the class MathOperations:
math_oper = MathOperations()
# math_oper2 =MathOperations()
# print(MathOperations())

# 2. Use this object math_oper to get the attributes:
x = math_oper.a
y = math_oper.b
z = math_oper.c

# print(f"x = {x}", f"y = {y}", f"z = {z}", sep="\n")

# 3. Using the object math_oper to get results or perform actions:
add = math_oper.addition()
sub = math_oper.subtraction()
div = math_oper.division()
multi = math_oper.multiplication()
# print(f"Addition = {add}")
# print(f"Subtraction = {sub}")
# print(f"Division = {div}")
# print(f"Multiplication = {multi}")

# As shown above instead of writing four different functions for math
# operations, we created one class that combines the four operations, and then
# we created different objects to get the results, the result is clean,
# readable and DRY code.
# That doesn't mean that classes are better than functions, or vice versa,
# because each one has its usage when writing the code and choosing the right
# approach is the programmer's decision.

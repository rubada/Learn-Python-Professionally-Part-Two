# Two types of variables can be defined inside the class:
# 1. Class variables or attributes are the variables that are defined inside
# the class, and outside of any class method.
# These variables can be shared across all the created objects, they belong to
# the class itself not to any specific instance (object).
# As discussed before when creating objects from a class each object has its
# own state or attributes, which are different for each object.
# This is not true for the class variables, different objects have the same
# class variables and can be used with these objects.

class MathOperations:
    # class attributes (class variable2s)
    a = 4
    b = 5
    c = 6

    # methods
    def addition(self):
        return self.a + self.b + self.c

    # Another way of accessing the class variable is using the class name
    # because these attributes belongs to the class itself.
    def subtraction(self):
        return MathOperations.a - MathOperations.b - MathOperations.c

    def multiplication(self):
        return self.a * self.b * self.c

    def division(self):
        return self.a / self.b


# The class attributes can be called using the class itself:
# print(MathOperations.a)
# print(MathOperations.b)
# print(MathOperations.c)

# Creating two objects and using the class attributes give the same result.
obj1 = MathOperations()
# print(obj1.a)
# print(obj1.subtraction())
# print("")
obj2 = MathOperations()
# print(obj2.a)
# print(obj2.subtraction())


# 2. Instance variables or attributes are the objects' attributes or states,
# and their values or states vary from object to object.
# How can they be defined?
# They can be defined using the __init__ constructor.

class MathOperations:
    # instance attributes or variables, __init__ constructor
    def __init__(self, a, b, c=0):
        self.a = a
        self.b = b
        self.c = c

    # methods
    def addition(self):
        return self.a + self.b + self.c

    def subtraction(self):
        return self.a - self.b - self.c

    def multiplication(self):
        return self.a * self.b * self.c

    def division(self):
        return self.a / self.b


# 1. Creating the first object
math_op_obj1 = MathOperations(2, 3, 5)
add_obj1 = math_op_obj1.addition()
sub_obj1 = math_op_obj1.subtraction()
div_obj1 = math_op_obj1.division()
multi_obj1 = math_op_obj1.multiplication()
# print("Object1")
# print(f"Addition object1 = {add_obj1}")
# print(f"Subtraction object1 = {sub_obj1}")
# print(f"Division object1 = {div_obj1}")
# print(f"Multiplication object1= {multi_obj1}")
# print("")

# 2. Creating the second object
math_op_obj2 = MathOperations(1, 2)
add_obj2 = math_op_obj2.addition()
sub_obj2 = math_op_obj2.subtraction()
div_obj2 = math_op_obj2.division()
multi_obj2 = math_op_obj2.multiplication()
# print("Object2")
# print(f"Addition object1 = {add_obj2}")
# print(f"Subtraction object1 = {sub_obj2}")
# print(f"Division object1 = {div_obj2}")
# print(f"Multiplication object1= {multi_obj2}")


# Class variables and instance variables can be used together.
# Let's consider a company that sells cars and we will create a class that
# calculates the sales percentage for different car brands.

class Sales:
    # creating a class variable that can be shared with all objects
    company_name = "Luxury Cars"

    # Creating the instance variables, by using the __init__ constructor
    def __init__(self, brand, total_brand_sold, total_cars_sold):
        self.brand = brand
        self.total_brand_sold = total_brand_sold
        self.total_cars_sold = total_cars_sold

    def sales_percentage(self):
        sales_per = self.total_brand_sold/self.total_cars_sold * 100
        return f"{Sales.company_name} sales percentage for \
{self.brand} brand = {int(sales_per)}%"


sales_car1 = Sales("Car1", 20000, 100000)
sales_car2 = Sales("Car2", 50000, 100000)
# print(sales_car1.sales_percentage())
# print(sales_car2.sales_percentage())

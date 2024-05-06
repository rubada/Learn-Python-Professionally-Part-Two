import math


# Let's take two examples on the benefits when the arithmetic operations
# return objects:
# Example 1:
class AddMul:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # Here we call the object and the attributes together
    def __add__(self, other):
        return AddMul(self.num1 + other.num1, self.num2 + other.num2)

    def __mul__(self, other):
        return self.num1 * other.num2

    def add_mul(self, other):
        # (self + other) will call __add__() will add 4 + 2 = 6 and 3 + 5 = 8,
        # result in AddMul(6, 8)
        # (self+other) * other will equal 6 * 5 = 30
        return (self+other) * other


add1_rev = AddMul(4, 3)
add2_rev = AddMul(2, 5)
# print(add1_rev.add_mul(add2_rev))


# Example 2:
# Now we will take an example of how to calculate the Euclidean distance
# between two points, using arithmetic operations dunder methods.
# Euclidean distance = √(x1 - x2)**2 + (y1 - y2)**2
# Euclidean distance for:
# point1 (x1, y1) = (2, 7)
# point2 (x2, y2)= (6, 13)
# is equal to 7.2111
class EuclideanDistance:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return EuclideanDistance(self.x - other.x, self.y - other.y)

    def __pow__(self, power):
        return math.pow(self.x, power) + math.pow(self.y, power)

    def euc_distance(self, other):
        return math.sqrt((self - other)**2)


point1 = EuclideanDistance(2, 7)
point2 = EuclideanDistance(6, 13)

euc_dist = point1.euc_distance(point2)

print("Euclidean distance between two points:", euc_dist)

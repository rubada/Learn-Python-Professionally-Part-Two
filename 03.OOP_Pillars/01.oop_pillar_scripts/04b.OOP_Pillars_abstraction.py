# The 4 Pillars of OOP in Python:
# 4. Abstraction:
# Also Abstraction is used, when you are working in projects, where you want
# to implement a common interface for the subclasses.

# Let's take an example to clear the abstraction concept:
from abc import ABC, abstractmethod
import math


class Shapes3d(ABC):

    @abstractmethod
    def total_surface_area(self):
        pass

    @abstractmethod
    def volume(self):
        pass

    @abstractmethod
    def diameter(self):
        pass

    @abstractmethod
    def diagonal(self):
        pass


class Cylinder(Shapes3d):

    def __init__(self, r, h):
        self.r = r
        self.h = h

    def total_surface_area(self):
        circular_base_area = 2 * math.pi * math.pow(self.r, 2)
        surface_area = 2 * math.pi * self.r * self.h
        cylinder_area = circular_base_area + surface_area
        return cylinder_area

    def volume(self):
        return self.h * math.pi * math.pow(self.r, 2)

    def diameter(self):
        return 2 * self.r

    def diagonal(self):
        return "A cylinder doesn't have a diagonal."


class RectanglePrism(Shapes3d):

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def total_surface_area(self):
        return 2 * (self.width * self.length + self.width * self.height
                    + self.length * self.height)

    def volume(self):
        return self.length * self.width * self.height

    def diameter(self):
        return "Rectangle Prism doesn't have a diameter."

    def diagonal(self):
        lwh_square = (math.pow(self.length, 2) + math.pow(self.width, 2) +
                      math.pow(self.height, 2))
        diagonal = math.sqrt(lwh_square)
        return diagonal


cylinder = Cylinder(3, 8)
# print(cylinder.diameter())
# print(cylinder.total_surface_area())
# print(cylinder.volume())
# print(cylinder.diagonal())

rectangle = RectanglePrism(3, 8, 6)
# print(rectangle.diagonal())
# print(rectangle.total_surface_area())
# print(rectangle.volume())
# print(rectangle.diameter())

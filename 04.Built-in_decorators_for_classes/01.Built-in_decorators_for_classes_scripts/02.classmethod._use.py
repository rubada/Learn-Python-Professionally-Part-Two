# Where and Why do we use classmethods?
# Factory methods, is a creational design pattern that is used to create
# objects with a common interface.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    @classmethod
    # Factory method
    def square(cls, side):
        # A square has equal sides, here we will return the class with two
        # parameters of the same name using the rectangle class.
        return cls(side, side)


rectangle = Rectangle(5, 3)
# print(f"Rectangle area: {rectangle.area()}")
# print(f"Rectangle Perimeter: {rectangle.perimeter()}")

# Create a square using the classmethod
square = Rectangle.square(4)
# print(square)
# print(f"Square area: {square.area()}")
# print(f"Square Perimeter: {square.perimeter()}")


# Using classmethod with factory method in inheritance
class Shape:

    def __init__(self, *args):
        # Defining the radius, the rectangle length and width or the triangle
        # base and height
        self.shape_data = []
        for i in args:
            self.shape_data.append(i)

    @classmethod
    def create_shape(cls, shape_type, *args):
        shape = eval(shape_type)
        return shape(*args)


class Circle(Shape):

    def area(self):
        """
        The attribute here is the circle radius.
        radius = self.shape_data[0]
        """
        # return self.shape_data
        return round(22 / 7 * self.shape_data[0]**2, 2)


class Rectangle(Shape):
    def area(self):
        """
        The attributes here are the rectangle length and width.
        length = self.shape_data[0]
        width = self.shape_data[1]
        """
        return round(self.shape_data[0] * self.shape_data[1], 2)


class Triangle(Shape):
    def area(self):
        """
        The attributes here are the triangle base and height.
        base = self.shape_data[0]
        height = self.shape_data[1]
        """
        return round(self.shape_data[0] * self.shape_data[1] / 2, 2)


shapes = {"Circle", "Rectangle", "Triangle"}

shape_type = input("Enter a shape type (circle, rectangle, or triangle): ")
shape_type = shape_type.lower().capitalize()

if shape_type in shapes:
    a = float(input("Type circle radius, rectangle width or triangle base:"))
    b = float(input("Type 0 if circle, rectangle length or triangle height:"))
    if shape_type == "Circle":
        shape_instance = Shape.create_shape(shape_type, a)
        print(shape_instance.area())
        # When using classmethod, it will create the correct instance of the
        # child class.
        print(isinstance(shape_instance,
                         eval(shape_type)))

    elif shape_type == "Rectangle" or shape_type == "Triangle":
        shape_instance = Shape.create_shape(shape_type, a, b)
        print(shape_instance.area())
        # When using classmethod, it creates the correct instance of the child
        # class.
        print(isinstance(shape_instance,
                         eval(shape_type)))
else:
    print(f"Invalid shape type: {shape_type}, choose from the three options \
shown.")

# As shown above instead of creating an instance for each shape we used the
# classmethod in order to use the class itself to get the result we need.

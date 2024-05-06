# Examples of dunder methods
# Here we will discuss the most used dunder methods.
# As discussed before dunder methods are invoked or called when the object is
# initiated.
# The below link shows all the dunder methods in Python docs, or you can check
# any other site you prefer:
# https://docs.python.org/3/reference/datamodel.html#special-method-names

# 5. object.__getattribute__(self, name), Python will invoke this method,
# whether the attribute exists or not, it is used to customize attribute
# access behavior. As shown below:
# https://docs.python.org/3/reference/datamodel.html#object.__getattribute__
class MainClass:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __getattribute__(self, name):
        if name == "num3":
            return 6
        else:
            return f"Attribute is available {name}"


obj_attr = MainClass(2, 4)
# print(obj_attr.num1)
# print(obj_attr.num3)


# Let's take another example:
class MainClassRev:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __getattribute__(self, name):
        if name not in ["num1", "num2"]:
            return (f"AttributeError: Attribue {name} is not found")
        else:
            # return object.__getattribute__(self, name)
            return super().__getattribute__(name)


obj_attr1 = MainClassRev(1, 6)
# print(obj_attr1.num1)
# print(obj_attr1.num3)


# Let's discuss some important points when using __getattribute__:
# 1. If __getattribute__() exists in your class it should return a value or
# should raise an exception.

# 2. When the attributes data type is a dictionary (table), a list, etc.,
# you can use the __getattribute__(), to check for an attribute availability or
# checking for the data type, data values type, etc.
# This point is important in attribute debugging.
# Let's take an example:

class ListOfNumbers:

    def __init__(self, data_list):
        self.data_list = data_list

    # Here we can use __getattribute__() to check the type of data used (list)
    # and check the data type inside "data_list", because __getattribute__ is
    # called as long as its exist inside the class.
    def __getattribute__(self, data):

        if data == "data_list":

            data_list = object.__getattribute__(self, data)

            if not isinstance(data_list, list):
                # Error Handling will be discussed in detail in Part 3 of this
                # course.
                raise TypeError(f"{data} attribute should be a LIST.")
            for num in data_list:
                # Error Handling will be discussed in detail in Part 3 of this
                # course.
                try:
                    int(num)
                except ValueError:
                    raise ValueError(f"({data}) attribute's items should be\
 an integer, not a float, or a string.")
            return super().__getattribute__(data)

        elif data == "__dict__":
            return super().__getattribute__(data)

        else:
            raise AttributeError(f"Attribue ({data}) is not found")


data = [1, 2, 5]
# data = 5
# data = [1, "5.5", 5]
# num_list = ListOfNumbers(data)
# print(num_list.data_list)
# print(num_list.num3)
# print(num_list.__dict__)


# 3. Using other methods inside the class, when __getattribute__ is used
# inside the class.

class MainClassRev2:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __getattribute__(self, name):

        if name in ["num1", "num2"]:
            return super().__getattribute__(name)

        elif name in ["add", "sub"]:
            return super().__getattribute__(name)

        else:
            return (f"AttributeError: Attribue {name} is not found")

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2


obj_attr2 = MainClassRev2(5, 4)
# print(obj_attr2.add())
# print(obj_attr2.sub())


# 4. Finally, remember when using __getattribute__ it is important to handle
# potential recursion carefully.
# Example:
class MainClassRev1:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __getattribute__(self, name):
        # Here when using "self" inside the __getattribute__ Python
        # will call or invoke the __getatribute__ again which will lead
        # to infinite recursion
        if name not in self.__dict__:
            return (f"AttributeError: Attribue {name} is not found")
        else:
            return super().__getattribute__(name)


obj_rec = MainClassRev1(1, 6)
# print(obj_rec.num1)


# __getattribute__ is a powerful tool, but misuse can lead to unexpected
# behavior.

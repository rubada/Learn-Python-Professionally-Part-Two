# Examples of dunder methods
# Here we will discuss the most used dunder methods.
# As discussed before dunder methods are invoked or called when the object is
# initiated.
# The below link shows all the dunder methods in Python docs, or you can check
# any other site you prefer:
# https://docs.python.org/3/reference/datamodel.html#special-method-names

# 4. object.__getattr__(self, name)
# This method is called when accessing an attribute returns an AttributeError,
# it will return a value, or raise an AttributeError exception.
# https://docs.python.org/3/reference/datamodel.html#object.__getattr__
class MainClass:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


obj = MainClass(5, 4)

# When calling obj attributes, Python will look for the object attributes in
# the object's dictionary attributes (__dict__):
# print(obj.num1)
# print(obj.num2)

# If the attributes were not found then Python will raise an AttributeError:
# print(obj.a)


# We can use the __getattr__ to remove this error.
# Here we will discuss some __getattr__() methods:
# 1. When using __getattr__ method, if the attribute is not found, Python will
# invoke this method and return a value or raise an error:
class MainClassRev:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __getattr__(self, name):
        if name.startswith("num"):
            return self.num1 + self.num2
        else:
            # This is returning a value not raising an AttributeError
            # exception, in the error handling section, we will talk about how
            # to raise an exception
            return f"AttributeError: Attribue '{name}' is not found"


obj_rev = MainClassRev(10, 6)
# print(obj_rev.num1)
# print(obj_rev.num2)
# print(obj_rev.a)
# print(obj_rev.num3)

attr_dict = obj_rev.__dict__
# print(obj_rev.__dict__)

# Adding the num3 to the attributes dictionary:
attr_dict["num3"] = 9
# print(obj_rev.__dict__)

# The result will be 9 not 16 when invoking num3:
# print(obj_rev.num3)

# Also we can use the getattr() to get the same result:
# print(getattr(obj_rev, "num4"))


# 2. Also, you can use the getattr() to set a default value for non-existing
# attributes:
class PersonName:

    def __init__(self, name):
        self.name = name

    def full_name(self, last):
        return f"{self.name} {last}"


name_obj = PersonName("John")

# Setting a value for non existing attributes:
name1 = getattr(name_obj, "name", "Mary")
# print(name1)

name2 = getattr(name_obj, "age", 20)
# print(name2)


# 3. Finally, here is an example of how to use the __getattr__():
class DataAccessing:

    def __init__(self, data_dict):
        self.data_dict = data_dict

    def __getattr__(self, name):
        if name in self.data_dict:
            return self.data_dict[name]
        else:
            return f"{type(self).__name__}' object has no attribute '{name}'"


# Define the data
data_dict = {
    "name": "John_Holland",
    'password': "Hello%469",
    "date_birth": "Feb 3, 1999",
    "gender": "Male",
    "occupation": "Engineer"
    }

person_data = DataAccessing(data_dict)

# Accessing the data
# print("Name:", person_data.name)
# print("Date of birth:", person_data.date_birth)
# print("Occupation:", person_data.occupation)
print("Leave Days:", person_data.leave_days)

# print(person_data.__dict__)

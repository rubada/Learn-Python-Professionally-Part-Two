# "property" Decorator:
# Some examples of where to use "property" decorator:
# 1. Create read-only attributes:
# Suppose you want to create attributes that can't be modified when
# the object's attribute is set.
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name_first(self):
        return self._name


# Creating an instance:
person = Person("Tom")
# print(person.name_first)

# Let's try to change the attribute of this instance
person.name_first = "Mary"
# print(person.name_first)

# As shown above, using the getter function only will make the attribute of an
# instance read-only because there is no setter method.
# This is a good practice if you don't want unintended modifications from
# outside the class.


# 2. Create read-write attributes:
# As shown in the TemperatureConvertor where we create a read-write attribute,
# to compute the temperature in Celsius and in Fahrenheit.


# 3. Create write-only attributes, when we create an attribute that can't be
# accessed, we only can write or set this attribute, like creating passwords
# or confidential information that must not be accessed or shown to others.
class ConfidInformation:

    @property
    def person_data(self):
        return "Information is confidential"

    @person_data.setter
    def person_data(self, account):
        # setting
        self._name = account[0]
        self._password = account[1]


# Getting the data
name = input("Insert name: ")
password = input("Insert Password: ")

# # Creating an instance
data = ConfidInformation()

# # Setting or inserting the data in the system:
data.person_data = [name, password]

# # Try to get the data:
print()
print(data.person_data)

# 4. Data Validation, inside the setter function you can add an "if" statement
# to check if the data is valid or not according to your code.

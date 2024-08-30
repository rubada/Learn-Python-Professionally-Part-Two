# "property" decorator
# "property" decorator is a built-in decorator in Python which is helpful in
# defining the properties without manually calling the built-in
# function property(). The decorator allows you to create a property object or
# attribute of a class, same as the "property()"
# The difference is that the methods that have the property function as a
# decorator will not be protected members because the methods that have the
# getter decorator will be called from outside the class.

class TemperatureConvertor:

    """Fahrenheit to Celsius"""
    # 1. Add the property decorator on the get function:
    @property
    def temp_get_fahrenheit(self):
        """Get the temperature in Fahrenheit"""
        return self._fahrenheit

    # 2. Define the setter decorator, we can keep the same name as the
    # get function.
    @temp_get_fahrenheit.setter
    def temp_set_fahrenheit(self, fahrenheit):
        """Set the temperature in Fahrenheit"""
        self._fahrenheit = fahrenheit

    # 3. We can add a deleter function
    @temp_get_fahrenheit.deleter
    def temp_del_fahrenheit(self):
        del self._fahrenheit

    def convert_to_celsius(self):
        celsius = (self._fahrenheit - 32) * 5/9
        print(f"The {self._fahrenheit}°F is:")
        return f"{round(celsius, 0)}°C"

    """Celsius to Fahrenheit"""
    @property
    def temp_get_celsius(self):
        """Get the temperature in Celsius"""
        return self._celsius

    @temp_get_celsius.setter
    def temp_set_celsius(self, celsius):
        """Set the temperature in Celsius"""
        self._celsius = celsius

    @temp_get_celsius.deleter
    def temp_del_celsius(self):
        del self._celsius

    def convert_to_fahrenheit(self):
        fahrenheit = self._celsius * 9/5 + 32
        print(f"The {self._celsius}°C is:")
        return f"{round(fahrenheit, 0)}°F"


# Creating an instance of the the class
temp = TemperatureConvertor()

# celsius_or_fahrenheit = input("Choose C or F: ")
# if celsius_or_fahrenheit == "F":
#     fahrenheit = float(input("Insert temperature in Fahrenheit: "))
#     temp.temp_set_fahrenheit = fahrenheit
#     print(temp.convert_to_celsius())

# elif celsius_or_fahrenheit == "C":
#     celsius = float(input("Insert temperature in Celsius: "))
#     temp.temp_set_celsius = celsius
#     print(temp.convert_to_fahrenheit())

# else:
#     print("Wrong input, please insert C or F in capital letters")


temp.temp_set_celsius = 90
# print(temp.convert_to_fahrenheit())

# Get the property:
# print(temp.temp_get_celsius)

# Deleting the property:
del temp.temp_del_celsius
# print(temp.temp_get_celsius)

# If we try and print the attribute, it will give an AttributeError,
# saying that 'TemperatureConvertor' object has no attribute '_celsius'


# Final note in the above example, we didn't use the __init__(), but if your
# code needs to add public attributes you can use the __init__, also you can
# use these attributes with the property function if needed.

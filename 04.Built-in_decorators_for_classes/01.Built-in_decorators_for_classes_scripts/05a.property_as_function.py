# "property()" Function:
# The property() function is a built-in function that allows you to create a
# property object. This property object then defines how an attribute can be
# accessed or modified.
# Let's take an example:
# Let's say you want to create a class to covert the temperature to either
# Celsius or Fahrenheit, as shown below:
class TemperatureConvertor:
    def __init__(self, celsius, fahrenheit):
        self.celsius = celsius
        self.fahrenheit = fahrenheit

    def to_fahrenheit(self):
        print("Temperature in Fahrenheit")
        return round(self.celsius * 9/5 + 32, 0)

    def to_celsius(self):
        print("Temperature in Celsius")
        return round((self.fahrenheit - 32) * 5/9, 0)


# To use the above class you will define an instance with both temperature
# values and then do the conversion, as shown below:
temp_convert = TemperatureConvertor(20, 80)

# Then call each methods separately:
# print(temp_convert.to_fahrenheit())
# print(temp_convert.to_celsius())


# As shown above, when a user uses the above code, he needs to add the
# temperature in both Celsius and Fahrenheit, this is a simple code, and it is
# not practical, but how can you write a professional temperature converter,
# of course, we can use the property function.
# First, let's check the property() syntax:
# property(fget=None, fset=None, fdel=None, doc=None)
# fget is a function to get the value of the attribute.
# fset is a function to set the value of the attribute.
# fdel is a function to delete the attribute.
# doc is a string (like a comment).
# When using property(), it is recommended to use protected members with it,
# to inform the one who is using the code that these members can't be accessed
# from outside.
# Example:
class TemperatureConvertorRev:

    # First, create the get and the set functions to convert the temperature
    # from Fahrenheit to Celsius:
    def _get_temp_fahrenheit(self):
        """Get the temperature in Fahrenheit"""
        return self._fahrenheit

    def _set_temp_fahrenheit(self, fahrenheit):
        """Set the temperature in Fahrenheit"""
        self._fahrenheit = fahrenheit

    def convert_to_celsius(self):
        celsius = (self._fahrenheit - 32) * 5/9
        print(f"The {self._fahrenheit}°F is:")
        return f"{round(celsius, 0)}°C"

    # Secondly, create the get and the set functions to convert the
    # temperature from Celsius to Fahrenheit:
    def _get_temp_celsius(self):
        """Get the temperature in Celsius"""
        return self._celsius

    def _set_temp_celsius(self, celsius):
        """Set the temperature in Celsius"""
        self._celsius = celsius

    def convert_to_fahrenheit(self):
        fahrenheit = self._celsius * 9/5 + 32
        print(f"The {self._celsius}°C is:")
        return f"{round(fahrenheit, 0)}°F"

    # Use the property() to define fahrenheit_to_celsius property to return the
    # temperature in Celsius:
    fahrenheit_to_celsius = property(_get_temp_fahrenheit,
                                     _set_temp_fahrenheit)

    # Use the property() to define celsius_to_fahrenheit property to return the
    # temperature in Fahrenheit:
    celsius_to_fahrenheit = property(_get_temp_celsius,
                                     _set_temp_celsius)


# Creating an instance of the the class
temp = TemperatureConvertorRev()

celsius_or_fahrenheit = input("Choose C or F: ")
if celsius_or_fahrenheit == "F":
    fahrenheit = float(input("Insert temperature in Fahrenheit: "))
    temp.fahrenheit_to_celsius = fahrenheit
    print(temp.convert_to_celsius())
elif celsius_or_fahrenheit == "C":
    celsius = float(input("Insert temperature in Celsius: "))
    temp.celsius_to_fahrenheit = celsius
    print(temp.convert_to_fahrenheit())
else:
    print("Wrong input, please insert C or F in capital letters")

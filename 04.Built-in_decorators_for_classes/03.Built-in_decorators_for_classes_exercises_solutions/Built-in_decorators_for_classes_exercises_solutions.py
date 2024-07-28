# 1rst Question
# Create a temperature converter to convert a given temperature to a different
# temperature scales:
# 1. Celsius to Fahrenheit and Kelvin
# 2. Fahrenheit to Celsius and Kelvin
# 3. Kelvin to Celsius and Fahrenheit
# Try to make your code a better code than the one we wrote in the scripts,
# D.R.Y. (Don't Repeat Yourself)

# Solution
class TemperatureConverter:

    # Use the property decorator to get and set the temperature
    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        self._temperature = temperature

    # Use the property decorator to get and set the temperature scale.
    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, scale):
        # Beware setter method doesn't return a value use raise instead.
        if scale not in ("C", "F", "K"):
            raise ValueError("Invalid scale {scale}. Input sacles: C\
 for Celsius, F for Fahrenheit, and K for Kelvin")
        self._scale = scale

    def celsius_to_fahrenheit(self):
        fahrenheit = self._temperature * 9/5 + 32
        print(f"The {self._temperature}°C is:")
        return f"{round(fahrenheit, 0)}°F"

    def celsius_to_kelvin(self):
        kelvin = self._temperature + 273.15
        print(f"The {self._temperature}°C is:")
        return f"{kelvin}K"

    def fahrenheit_to_celsuis(self):
        celsius = (self._temperature - 32) * 5/9
        print(f"The {self._temperature}°F is:")
        return f"{round(celsius, 0)}°C"

    def fahrenheit_to_kelvin(self):
        kelvin = (self._temperature + 459.67) * 5/9
        print(f"The {self._temperature}°F is:")
        return f"{round(kelvin, 2)}K"

    def kelvin_to_celsius(self):
        celsius = self._temperature - 273.15
        print(f"The {self._temperature}K is:")
        return f"{round(celsius, 0)}°C"

    def kelvin_to_fahrenheit(self):
        fahrenheit = self._temperature * 9/5 - 459.67
        print(f"The {self._temperature}K is:")
        return f"{round(fahrenheit, 0)}°F"


scale = "K"
temperature = 60
temp_F = TemperatureConverter()
temp_F.scale = scale
temp_F.temperature = temperature
if scale == "C":
    print(temp_F.celsius_to_fahrenheit())
    print(temp_F.celsius_to_kelvin())

elif scale == "F":
    print(temp_F.fahrenheit_to_celsuis())
    print(temp_F.fahrenheit_to_kelvin())

else:
    print(temp_F.kelvin_to_celsius())
    print(temp_F.kelvin_to_fahrenheit())

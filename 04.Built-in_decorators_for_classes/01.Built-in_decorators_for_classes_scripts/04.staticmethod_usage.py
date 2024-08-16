from datetime import date
import re
# Where do you use staticmethod()?
# Utility Functions:
# Utility functions in Python are simple, reusable functions, have a specific
# task, and they can be used accross different part in our code.
# These functions are not meant to be standalone, but rather to be used in
# conjunction with other code. They can be called from within other functions,
# scripts, or modules.
# Utility functions are often used for common tasks, such as the following
# built-in functions:
# 1. Mathematical operations, such as max(), min(), sum(), etc.
# 2. File I/O, such as open().
# 3. "len()" Function.
# 4. "sorted()" function.
# etc.
# Also we can create user-defined utility functions:


# Example:
def num_square(number):
    """Calculate the square of a number"""
    return number * number


x = 6
# print(f"Number {x} Square is:", num_square(x))
# The above function this function is precise, compact and reusable.


# These functions can be used inside a class with the stattic method, as shown
# below:
class PersonData:

    def __init__(self, full_name, date_of_birth):
        self.full_name = full_name
        self.date_of_birth = date_of_birth

    def age(self):
        "Date format is year-month-day"
        date_list = self.date_of_birth.split("-")
        age = date.today().year - int(date_list[0])
        return age

    @staticmethod
    def is_date_valid(date_str, seperator):
        day, month, year = map(int, date_str.split(seperator))
        if day <= 31 and month <= 12 and year <= 2024:
            return True
        else:
            return False

    @staticmethod
    def date_correct_format(date_str, separator):
        day, month, year = date_str.split(separator)
        return "-".join([year, month, day])


# person_data = input("Enter full name and birth date seperate by comma:")
person_data = "Mary Hill, 24/4/2001"
person_data = person_data.split(", ")
seperator = re.sub("[0-9]", "", person_data[1])[0]
# print(seperator)

date_validation = PersonData.is_date_valid(person_data[1], seperator)


if date_validation:
    date_coorect_format = PersonData.date_correct_format(person_data[1],
                                                         seperator)

    # Create a class instance
    person_details = PersonData(person_data[0], date_coorect_format)
    # print(f"{person_details.full_name} age is {person_details.age()}")
else:
    print("Date should be a numbers, with this order:\n\
day <= 31,\nmonth <= 12,\nyear <= present year")

# print(date_coorect_format)


# The last thing is we can call the static methods from the subclass
class child(PersonData):

    def age(self, separator):
        data_validation = PersonData.is_date_valid(self.date_of_birth,
                                                   separator
                                                   )
        if data_validation:
            date_coorect_format = PersonData.date_correct_format(
                self.date_of_birth,
                separator
                )
        else:
            print("Date should be a numbers, with this order:\n\
        day <= 31,\nmonth <= 12,\nyear <= present year")

        self.date_of_birth = date_coorect_format
        return PersonData.age(self)


obj = child("name", "24.3.2010")
seperator = re.sub("[0-9]", "", obj.date_of_birth).strip(" ")[0]
# print(obj.age(seperator))

# Why __repr__() and __str__() are important?
# The __str__() and __repr__() methods play essential roles in representing
# objects.
# Also str() and repr() are built-in functions in Python.
# https://docs.python.org/3/library/functions.html
# Let's take an example to show the difference between __str__ and __repr__:
import datetime

today_date = datetime.datetime.today()
# print(today_date)
# print(type(today_date))
# print()

# __str__ can be used such as str(), but str() is preferable:
# print("__str__() string:", today_date.__str__())
# print("str() string:", str(today_date))
# print(type(str(today_date)))
# print()

# __repr__ can be used such as repr(), but repr() is preferable:
# print("__repr__() string:", today_date.__repr__())
# print("repr() string:", repr(today_date))
# print(type(repr(today_date)))


# As shown in the output when using the repr() and str():
# 1. The output of the str() is the date in string format, which is a
# human-readable, informal string representation of an object.
# The str() output is intended for end users.

# 2. The output of repr() is the class instance, which is the official string
# representation of an object, this will allow us to reconstruct objects from
# their string representations, as shown when we used eval().

# 3. The repr() output is intended for developers and should be informative and
# clear. Developers use the repr() for debugging, and understanding the
# internal state of objects (attributes).
# Developers often use repr() during debugging to examine the internal state of
# an object, especially when dealing with custom classes or complex data
# structures.
# For example, if you have a custom class representing a user profile, the
# repr() method can display relevant information like the user’s ID, username,
# and other attributes.

# 4. In Python REPL (Read-Eval-Print Loop)* or Jupyter Notebook, evaluating an
# object directly displays its __repr__() representation, that's means the
# shell calls the repr() directly and evalute the object.
# *REPL (Read-Eval-Print Loop), is a tool that allows us to run Python, it is
# available in every Python installation.

# Let's take an example, using a user-defined class:

class Movie:

    def __init__(self, movie, actor):
        self.movie = movie
        self.actor = actor

    def __str__(self):
        return f"{self.movie} lead actor is {self.actor}"

    def __repr__(self):
        # If the attributes are string use single or double colons with
        # them, as shown below:
        return f"Movie(movie=\"{self.movie}\", actor='{self.actor}')"


movie = Movie("The Revenant", "Leonardo DiCaprio")
# print(movie)                # User-friendly output.
# print(type(movie))
# print()

# print(str(movie))           # User-friendly output.
# print(type(str(movie)))
# print()

# print(repr(movie))
# print(type(repr(movie)))    # For debugging and internal purposes.
print(eval(repr(movie)))

# Remember that using these methods appropriately in your code, will enhance
# code readability and maintainability.

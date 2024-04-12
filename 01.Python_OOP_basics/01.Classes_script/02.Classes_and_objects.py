# What are a class and objects?
# 1. A class is a category of things (objects) that have some properties in
# common and these properties differentiate it from other classes.
# Let's take cars for example, underneath the cars there are the brands,
# models, sizes, speed, etc., so the car is the general category or class (main
# object) that is used to create objects related to it, such as brands, sizes,
# number of wheels, speeds, etc., each one of them is an object that can be
# created from this car class.

# In Python classes are the blueprint or code template to create objects.
# To define a class, use the class keyword and then choose a class name, it is
# recommended (not compulsory) for the words in the class name to start with
# capital letters, without using an underscore to separate the words, if more
# than one word is used.
# Define a class:
class ClassName:
    # Class attributes (class variables)
    number = 10

    # Instance (object) attributes (instance variables)
    def __init__(self):
        pass

    # Behavior or object (instance) method
    def method_class(self):
        pass


# Create an instance or object
obj = ClassName()
# print(obj.number)
# print(obj.method_class())

# Creating an object or class instance is done by assigning the class to a
# variable.


# 2. Objects, as mentioned before everything in Python is an object, and
# objects are instances of a class, when a list is created as shown below:
numbers = [1, 2, 3]

# "numbers" is an instance or object of the list class, it is an object of the
# class and has a location in memory.

# Objects are collections of methods (behavior) and attributes (state).
# Below are the object properties:

# 1. State: It is the instance (object) attributes (instance variables), which
# reflects the object's properties or characteristics.

# For example in the Shoe Shop, the defined attributes or states:
# Number of shoes
# Shoe type
# Employee name
# Salespeople name
# color
# size
# etc.

# When using the above attributes to create objects, each object will have a
# different attribute, as shown below.

# Shoe type = “heels”
# Quantity = 50
# Salesperson name = “Tom”
# color = "red"
# size = "36"
# The above attributes or states of the "heel1" object reflect the properties
# and characteristics for this object.

# If other attributes are created as shown below:
# Shoe type = “heels”
# Quantity = 50
# Salesperson name = “Sam”
# color = "red"
# size = "39"

# This is another object, although it shares some properties with "heel1"
# object but they are the state or properties of the second object.

# An important note that even the above objects share some properties and
# their states have common representation, none of these objects shares
# the memory location, meaning the shoe type in the first object has
# a different memory location than the shoe type of object2, because they are
# two different objects.

# 2. Behavior: It is the object (instance) method, it is how the objects act
# on itself or reacts to other objects, changing or using the object states or
# attribute.
# Thus, the behavior of an object is a way to perform actions.

# In the Shoe Shop, the object "heel1" has many attributes, using these
# attributes to:
# Calculate Cost
# Calculate Profit
# Check if the shoe type is popular
# etc.

# The above operations are the behavior and actions (methods) the object does
# on the states (attributes) to get some results.

# 3. Identity: Every object should have a unique name, used to give it and
# identify and differentiate it from other objects.
# In the above example, "heel1" is a unique name for this object.

# Note: the object's state or attributes will be defined using the init dunder
# method which will be discussed in detail later.
# The objects variables are called the instance attributes.

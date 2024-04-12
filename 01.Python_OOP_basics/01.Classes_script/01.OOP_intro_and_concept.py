# Object-Oriented Programming (OOP)
# OOP is a programming languages paradigm, where classes and objects are used.
# Objects in OOP are the same as any system components, remember the shoe shop
# where the shop is a class (main object, system), while the salesperson, other
# employees, the goods, etc., are all objects (components) inside the shop
# serve the main purpose of the shoe shop, and that is selling shoes.
# OOP has similarities to the shoe shop, where the class has a purpose and the
# objects inside the class serve that purpose, and from the class, an object
# can be created
# Let's take an example, the list class:

nums = [7, 5, 1, 6, 4, 3, 2]

# "nums" is an object created from the list class

# print(type(nums))

# The list class has many methods or functions, when using these methods with
# the list object (nums), we can modify or change the list object (nums), to
# create the final list, which is the class's main purpose.
nums.append(9)
nums.sort()
num_pop = nums.pop()
# print(nums)
# print(num_pop)

# OOP is used to bind the objects (data and functions) work together as a
# single unit (class), in which these objects inside the class are isolated
# from the outside scope, and used to serve the purpose of this class.

# In OOP there are six concepts, that should be taken in account:

# The first two concepts are:
# 1. Classes
# 2. Objects

# The other four concepts are called the four pillars of object-oriented
# programming:
# 1. Inheritance
# 2. Polymorphism
# 3. Encapsulation
# 4. Abstraction

# When writing classes, same as functions, your code will be:
# 1. Clean.
# 2. Readable.
# 3. D.R.Y Don't Repeat Yourself.

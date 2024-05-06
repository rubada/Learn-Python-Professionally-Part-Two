# 1st Question:
# Create a class "Books" to return "True" if both books have the same
# published years:
# book1 = Books("Rise of the Knight", 1955)
# book2 = Books("Different People", 1955)
# print(book1 == book2)
# Output = True


# 2nd Question:
# Change below decorator to a class decorator that accepts arguments:
# def multiply_add(x, y):
#     def inner_deco(func):
#         def wrapper(*args, **kwargs):
#             z = func(*args, **kwargs) * 10 + x + y
#             return z
#         return wrapper
#     return inner_deco


# @multiply_add(2, 3)
# def add(a, b):
#     return a + b

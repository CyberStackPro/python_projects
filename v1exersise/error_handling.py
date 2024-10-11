# try:
#     #  with open("error_handling.py") as file:
#     file = open("error_handling.py") as file
#     age = int(input('Age: '))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age")
# else:
#     print('No exceptions were thrown.')
# finally:
#     file.close()


# Raising Exception

# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError('Age can not be 0 or less.')
#     return 10 / age


# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     print(error)

# Cost of Raising Exception
from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError('Age can not be 0 or less.')
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
   pass
"""


# best way
code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

    

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print("first code=", timeit(code1, number=10000))
print("second code=", timeit(code2, number=10000))

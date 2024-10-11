# creating our own func

# 1- Perform task
# 2- Return a value
# def name(name):
#  print(f"Hi {name}")


# param input for greet function
# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     return
#     # print(first_name, last_name)

# # arg actual value for greet function
# greet('Yeabsra', 'Gebriel')

# *args
# def multiply(*number):
#     count = 1
#     for num in number:
#         count += num
#     return count


# print(multiply(1, 2, 3, 4))

# **args
# def save_user(**user):
#     print(user['name'])


# save_user(id=1, name='John', age=22)

# scope

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total += number
#     return total


# print('Start')
# print(multiply(1, 2, 3, 4))

def fizz_buzz(input):
    # if not input % 3==0 or not input %  5 ==0:
    #     return input
    if (input % 3 == 0) and (input % 5 == 0):
        return 'FIZZ BUZZ'
    if input % 3 == 0:
        return 'FIZZ'
    if input % 5 == 0:
        return 'BUZZ'
    return input


print(fizz_buzz(30))

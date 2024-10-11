# List
# letter = ['a', 'b', 'c']
# matrix = [[0, 1], [2, 3]]
# zeros = [0] * 5

# combined = zeros + letter
# numbers = list(range(20))
# # chars = list('Hello world')
# chars = list(range(20))

# print(len(chars))
# print(numbers)
# print(combined)
# print(matrix)
# print(zeros)


# letter = ['a', 'b', 'c', 'd']
# letter[0] = 'A'
# print(letter[0:3])
# print(letter[::2])
# numbers = list(range(20))
# num2 = [1, 2, 3, 4, 5]
# print(num2[0::4])
# print(numbers[::2])

# numbers = [1, 2, 3]  # packing
# first = numbers[0]
# first, second, *other = numbers  # unpack

# print(first, other)

# for index, letter in enumerate(letters):
#     print(letter, index)

# letters = ['a', 'b',  'c']
# # Add
# letters.append('d')
# letters.insert(0, '_')

# # Remove
# letters.pop(0)
# # letters.remove('b')
# del letters[0:3]
# letters.clear()

# letters = ['a', 'b',  'c']
# numbers = [2, 4, 5, 6, 1, 2, 8, 9]
# numbers.sort(reverse=True)
# print(sorted(numbers))
# print(numbers)

# print(letters.index('b'))

# items = [
#     ('Product1', 80),
#     ('Product2', 20),
#     ('Product3', 60),
#     ('Product3', 6)
# ]
# def sort_items(items):
#     return items[1]
# items.sort(key=sort_items)
# better way of writhing this code
# items.sort(key=lambda item: item[1])

# print(items)
# items.sort()
# print(items)

# prices = []
# for item in items:
#     prices.append(item[1])

# print(prices)

# mapping
# prices = list(map(lambda item: item[1], items))
# Comprehension
# prices = [item[1] for item in items]
# print(prices)

# filtering mapping
# filtered = list(filter(lambda item: item[1] >= 10, items))
# Comprehension filtering
# filtered = [item for item in items if item[1] > 10]
# print(filtered)

# Zip
# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# zipped = list(zip(list1, list2))

# print(zipped)

# Stacks
# browsing_session = []
# # Adding
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)

# # Removing
# browsing_session.pop()

# if not browsing_session:
#     browsing_session[-1]
# print(browsing_session)

# Queues
# from collections import deque
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# # queue.popleft()
# queue.append(4)
# queue.append(5)
# queue.append(6)
# queue.popleft()

# print(queue)

# Tuples
# point = tuple('Hello World')
# point = (1, 2, 3)

# x, y, z = point
# if 1 in point:
#     print('exist')
# else:
#     print("not there")

# Swapping
# x = 10
# y = 11

# z = x # 10

# x = y # 11
# y = z # 10

# simpler way
# x, y = y, x
# print('X', x, "Y", y)

# Array
# from array import array
# numbers = array('i', [1, 2, 3])


# Sets
# numbers = [1, 1, 2, 3, 4]
# first = set(numbers)

# second = {1, 2, 4, 5}

# print(first | second)
# print(first & second)
# print(first - second)
# print(first ^ second)

# Dictionaries
# point = {'x': 1, 'y': 2}
# point = dict(x=1, y=2)
# point['x'] = 10
# point['z'] = 20

# del point['z']
# # first way
# for key in point:
#     print(key, point[key])

# second way
# for key, value in point.items():
#     print(key, value)
# print(point)

# Dictionary Comprehensions
# values = []
# for x in range(5):
#     values.append(x * 2)
# from sys import getsizeof
# values = (x * 2 for x in range(1))

# values = [x * 2 for x in range(10000)]
# print("Generate Size: ", getsizeof(values))

# Unpacking Operation
# numbers = [1, 2, 3]
# print(*numbers)
# # after
# print(numbers)
# print(1, 2, 3)
# values = list(range(5))
# values = [*range(5), *'Hello']
# print(values)
# first = {'x': 1}
# second = {'x': 10, 'y': 2}
# combined = {**first, **second, 'z': 1}
# print(combined)


# Ex
# from pprint import pprint
# Solution 1
# sentence = 'This is a common interview question is common'

# # Step 1: Split the sentence into words
# words = sentence.split()

# word_count = {}
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# repeated_words = [word for word, count in word_count.items() if count > 1]
# print(repeated_words)

# Solution 2
from pprint import pprint

sentences = 'This is a common interview question common '

char_frequency = {}
for char in sentences:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# print(char_frequency)
char_frequency_sorted = sorted(
    char_frequency.items(), key=lambda kv: kv[1], reverse=True)
# pprint(char_frequency, width=1)
print(char_frequency_sorted[0])

# letters = 'This is a common interview question is common'

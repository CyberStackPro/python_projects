#  Class: blueprint for creating new object
# Object: instance of class

# Class: Human
# Objects: John, Marry, Jack

# class Point:
#     def draw(self):
#         print('draw')
# @classmethod
# def zero(cls):
#     return cls(0, 0)

# point = Point()
# print(type(point))
# print(isinstance(point, int))

# class Point:
#     default_color = 'red'

#     def __init__(self, x, y):  # magic method
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# # Point.default_color = 'Yellow'

# # print(Point.default_color)
# point = Point(1, 2)
# # point.draw()
# # point.zero()
# # point.draw()
# print(point)

# Comparison Magic method

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)


# point = Point(10, 20)
# other = Point(1, 2)

# print(point == other)
# print(point > other)
# print(point + other)
# combined = point + other
# print(combined.x, combined.y)

# Basic method
# class WordCounter:
#     def __init__(self):
#         self.word_counts = {}

#     def add(self, word):
#         word = word.lower()
#         self.word_counts[word] = self.word_counts.get(word, 0) + 1


# counter = WordCounter()
# sentence = "Hello world world python Python hello"
# for word in sentence.split():
#     counter.add(word)

# print(counter.word_counts)

# Intermediate method
# class WordCounter:
#     def __init__(self):
#         self.word_counter = {}

#     def add(self, word):
#         word = word.lower()
#         self.word_counter[word] = self.word_counter.get(word, 0)+1

#     def count(self, word):
#         return self.word_counter.get(word.lower(), 0)


# # Example usage:
# counter = WordCounter()
# sentence = "Python is great and Python is fun"
# for word in sentence.split():
#     counter.add(word)

# # {'python': 2, 'is': 2, 'great': 1, 'and': 1, 'fun': 1}
# print(counter.word_counter)
# print(counter.count('python'))  # 2


# Advanced method
# class CustomTagCloud:
#     def __init__(self, allowed_tags=None):
#         self.tags = {}
#         self.allowed_tags = allowed_tags or []

#     def add(self, tag):
#         tag = tag.lower()
#         if self.allowed_tags and tag not in self.allowed_tags:
#             print(f"{tag} is not allowed.")
#             return
#         self.tags[tag] = self.tags.get(tag, 0) + 1

#     def count(self, tag):
#         return self.tags.get(tag.lower(), 0)

#     def __str__(self):
#         return str(self.tags)


# # Example usage:
# cloud = CustomTagCloud(allowed_tags=['python', 'java', 'javascript'])
# cloud.add('Python')
# cloud.add('JavaScript')
# cloud.add('C++')  # This will print "c++ is not allowed."

# print(cloud)  # Output: {'python': 1, 'javascript': 1}


# class TagCloud:
#     # __init__ Method (Constructor):
#     def __init__(self):
#         self.__tags = {}

#     def add(self, tag):
#         # self.tags.get(key, default)
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):
#         return self.__tags.get(tag.lower(), 0)

#     def __setitem__(self, tag, count):
#         self.__tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.__tags)

#     def __iter__(self):
#         return iter(self.__tags)


# cloud = TagCloud()
# # cloud['python'] = 10
# # we can access the __tags with this
# print(cloud.__dict__)
# cloud.add('python')
# cloud.add('python')
# cloud.add('python')
# cloud.add('python')

# # to get length
# # print(cloud.__len__())

# # print(cloud.__tags['Python'])
# print(cloud._TagCloud__tags)

# class Product:
#     def __init__(self, price):
#         self.price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError('Price cannot be negative.')
#         self.__price = value

#     # /  and we can apply this by using decorator like @property on the header of the function
#     # price = property(get_price, set_price)


# product = Product(10)
# # print(product.price)
# # product.price = -1
# print(product.price)


#  Animal: Parent, Base
#  Mammal: Child, sub
# class Animal:
#     def __init__(self):
#         print('Animal Constructor')
#         self.age = 1

#     def eat(self):
#         print('eat')


# class Mammal(Animal):
#     def __init__(self):
#         # calling it first
#         print('Mammal Constructor')
#         self.weight = 1
#         super().__init__()

#         # calling it after
#         # super().__init__()
#         # print('Mammal Constructor')
#         # self.weight = 1

#     def walk(self):
#         print('walk')


# class Fish(Animal):
#     def swim(self):
#         print('swim')


# m = Mammal()
# # print(isinstance(m, object))
# # print(issubclass(Mammal, object))

# print(m.age)
# print(m.weight)


# class Animal:
#     def eat(self):
#         print('eat')


# class Bird(Animal):
#     def fly(self):
#         print('fly')


# class Chicken(Bird):
#     pass


# Employee - Person - LivingCreature - Thing

# class Employee:
#     def greet(self):
#         print('Employee Greet')


# class Person:
#     def greet(self):
#         print('Person Greet')


# class Manager(Employee, Person):
#     pass


# manager = Manager()

# manager.greet() // Employee greet b/c we put in the manager argument Employee first

#  a good example of multiple inheritance
# class Flyer:
#     def fly(self):
#         pass


# class Swimmer:
#     def swim(self):
#         pass


# class FlyingFish(Flyer, Swimmer):
#     pass


# Stream of Data
# from abc import ABC, abstractmethod


# class InvalidOperationError(Exception):
#     pass


# class Stream(ABC):
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError('Stream is already open')
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError('Stream is already closed')
#         self.opened = False

#     @abstractmethod
#     def read(self):
#         pass


# class FileStream(Stream):
#     def read(self):
#         print('Reading data from a file')


# class NetworkStream(Stream):
#     def read(self):
#         print('Reading data from a network')


# class MemoryStream(Stream):
#     def read(self):
#         print('Reading data from a memory stream')


# stream = Stream()

# print(stream.open())
# print(stream.read())

from abc import ABC, abstractmethod


class UIControl(ABC):
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print('TextBox')


class DropDownList(UIControl):
    def draw(self):
        print('DropDown List')


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()
# print(isinstance(ddl, UIControl))
draw([ddl, textbox])
# draw(ddl)

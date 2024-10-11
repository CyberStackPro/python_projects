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


class TagCloud:
    # __init__ Method (Constructor):
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        # self.tags.get(key, default)
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)


cloud = TagCloud()
cloud['python']
cloud.add('Python')
cloud.add('Python')
cloud.add('python')
print(cloud.tags)

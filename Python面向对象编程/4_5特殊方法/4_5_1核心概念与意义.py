# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(1, 2)
# p2 = Point(3, 4)

# print(p1)
# print(p1 + p2)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'Point({self.x}, {self.y})'
#
#
#
# p1 = Point(1, 2)
# print(p1)
# print(str(p1))

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'Point({self.x}, {self.y})'
#
#     def __add__(self, other):
#         if isinstance(other, Point):
#             new_x = self.x + other.x
#             new_y = self.y + other.y
#             return Point(new_x, new_y)
#         raise TypeError('只能和 Point 对象相加')

# p1 = Point(1, 2)
# p2 = Point(3, 4)
# p3 = p1 + p2
# print(p3)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'Point({self.x}, {self.y})'
#
#     def __add__(self, other):
#         if isinstance(other, Point):
#             new_x = self.x + other.x
#             new_y = self.y + other.y
#             return Point(new_x, new_y)
#         raise TypeError('只能和 Point 对象相加')
#
#     def __getitem__(self, key):
#         if key == 0 or key == 'x':
#             return self.x
#         elif key == 1 or key == 'y':
#             return self.y
#         raise KeyError(f'无效的键: {key}')

# p = Point(1, 2)
# print(p[0])
# print(p['y'])

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'Point({self.x}, {self.y})'
#
#     def __add__(self, other):
#         if isinstance(other, Point):
#             new_x = self.x + other.x
#             new_y = self.y + other.y
#             return Point(new_x, new_y)
#         raise TypeError('只能和 Point 对象相加')
#
#     def __getitem__(self, key):
#         if key == 0 or key == 'x':
#             return self.x
#         elif key == 1 or key == 'y':
#             return self.y
#         raise KeyError(f'无效的键: {key}')
#
#     def __len__(self):
#         return 2

# p = Point(1, 2)
# print(len(p))

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     # def __str__(self):
#     #     return f'Point({self.x}, {self.y})'
#
#     def __repr__(self):
#         return f'Point(x={self.x}, y={self.y})'
#
#     def __add__(self, other):
#         if isinstance(other, Point):
#             new_x = self.x + other.x
#             new_y = self.y + other.y
#             return Point(new_x, new_y)
#         raise TypeError('只能和 Point 对象相加')
#
#     def __getitem__(self, key):
#         if key == 0 or key == 'x':
#             return self.x
#         elif key == 1 or key == 'y':
#             return self.y
#         raise KeyError(f'无效的键: {key}')
#
#     def __len__(self):
#         return 2
#
# p = Point(1, 2)
# print(p)
# print(repr(p))

class MyList:
    def __init__(self, items):
        self.items = items

    def __str__(self):
        return f'MyList: {self.items}'

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __add__(self, other):
        if isinstance(other, MyList):
            return MyList(self.items + other.items)
        raise TypeError('只能和 MyList 对象相加')

    def __eq__(self, other):
        if isinstance(other, MyList):
            return self.items == other.items
        return False

lst1 = MyList([1, 2, 3])
lst2 = MyList([4, 5, 6])

print(lst1)
print(lst2)

print(len(lst1))
print(lst1[0])

lst1[0] = 10
print(lst1)

lst3 = lst1 + lst2
print(lst3)

print(lst1 == lst2)
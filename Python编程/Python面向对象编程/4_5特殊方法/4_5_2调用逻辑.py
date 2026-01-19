# class Point:
#     def __init__(self, x, y):
#         print('__init__ 被调用了!')
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         print('__str__ 被调用了!')
#         return f'Point({self.x}, {self.y})'
#
#     def __repr__(self):
#         print('__repr__ 被调用了!')
#         return f'Point(x={self.x}, y={self.y})'
#
#     def __add__(self, other):
#         print('__add__ 被调用了!')
#         if isinstance(other, Point):
#             return Point(self.x + other.x, self.y + other.y)
#         return NotImplementedError
#
#     def __radd__(self, other):
#         print(f'__radd__ 被调用了!')
#         return self.__add__(other)

# p1 = Point(1, 2)
# p2 = Point(3, 4)

# p3 = p1 + p2
# print(p3)

# p4 = 0 + p1
# print(p4)

# p = Point(1, 2)
# # print(p.x, p.y)
# # print(p)
# # print(str(p))

class MyList:
    def __init__(self, items):
        self.items = items

    def __str__(self):
        return f'MyList: {self.items}'

    def __len__(self):
        print(f'__len__ 被调用了!')
        return len(self.items)
        # return -1

    def __getitem__(self, key):
        print(f'__getitem__ 被调用，key = {key}')
        return self.items[key]

    def __setitem__(self, key, value):
        print(f'__setitem__ 被调用，key = {key}')
        self.items[key] = value

lst = MyList([1, 2, 3])
# print(lst[0])

# print(lst[1: 3])
# lst[0] = 10
# print(lst[0])

# print(len(lst))

class Point:
    def __str__(self):
        return '类的 __str__'

p = Point()

p.__str__ = '实例的 __str__ '

# print(p.__str__)
# print(p)

class ShoppingCart:
    def __init__(self, goods):
        self.goods = goods
        print('购物车初始化完成!')

    def __str__(self):
        return f'购物车: {self.goods}'

    def __len__(self):
        return len(self.goods)

    def __getitem__(self, key):
        return self.goods.get(key, 0)

    def __setitem__(self, key, value):
        if value >= 0:
            self.goods[key] = value
        else:
            print(f'商品 {key} 数量不能为负!')

    def __add__(self, other):
        if isinstance(other, ShoppingCart):
            new_goods = self.goods.copy()
            for name, num in other.goods.items():
                new_goods[name] = new_goods.get(name, 0) + num

            return ShoppingCart(new_goods)
        return NotImplemented

cart1 = ShoppingCart({'苹果': 2, '香蕉': 3})
cart2 = ShoppingCart({'苹果': 1, '橙子': 4})

print(cart1)

print(len(cart1))

print(f'购物车 1 苹果数量: {cart1["苹果"]}')

cart1['香蕉'] = 5
print(cart1)
cart1['香蕉'] = -1

cart3 = cart1 + cart2
print(cart3)
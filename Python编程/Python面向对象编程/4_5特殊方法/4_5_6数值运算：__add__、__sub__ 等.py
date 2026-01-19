class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Point(self.x + other, self.y + other)

        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Point(self.x - other, self.y - other)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Point(self.x * other, self.y * other)

        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    # def add(self, other):
    #     return Point(self.x + other.x, self.y + other.y)

# p1 = Point(10, 20)
# p2 = Point(3, 4)
# # print(p1 - p2)
#
# # print(p1 * 2)
#
# # print(3 * p2)
#
# print(p1 - 5)

# p1 = Point(1, 2)
# p2 = Point(3, 4)
# # p3 = p1.add(p2)
# print(p1 + p2)
#
# # print(p1 + p2)
#
# print(p1 + 10)
# print(10 + p1)

# print(p3)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Product(self.name, self.price + other)

        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            new_price = max(0, self.price - other)
            return Product(self.name, new_price)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            total_price = self.price * other
            return f'{self.name} x {other} 件，总价: ￥{total_price:.2f}'

        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        return f'{self.name}，单价：¥{self.price:.2f}'

apple = Product('苹果', 5.99)
print(apple + 1)
print(apple - 2)

print(apple - 10)

print(apple * 5)
print(10 * apple)
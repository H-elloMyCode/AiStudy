# class ShoppingCart:
#     def __init__(self):
#         self.goods = {}
#
#     def __len__(self):
#         return sum(self.goods.values())
#
#     def __getitem__(self, key):
#         if not isinstance(key, str):
#             raise TypeError('商品名必须是字符串')
#         return self.goods.get(key, 0)
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise TypeError('商品名必须是字符串')
#         if not isinstance(value, int) or value < 0:
#             raise ValueError('商品数量必须是 >= 0 的整数')
#
#         if value == 0:
#             if key in self.goods:
#                 del self.goods[key]
#         else:
#             self.goods[key] = value
#
#     def get_goods_count(self):
#         return len(self.goods)
#
#     def get_goods_num(self, name):
#         return self.goods.get(name, 0)
#
#     def __str__(self):
#         res = ""
#         for key, value in self.goods.items():
#             res += f'{key}: {value} '
#         return res

# cart = ShoppingCart()
# cart.goods['苹果'] = 2
# cart.goods['香蕉'] = 3
#
# print(cart)
# cart['苹果'] = 5
# print(cart)
#
# cart['苹果'] = 0
# print(cart)

# print(cart['苹果'])
# print(cart['香蕉'])
# print(cart[1])

# print(len(cart))
# print(cart.get_goods_count())
# print(cart.get_goods_num('苹果'))

# print(len(cart))

class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, key):
        return self.items[key]

# lst = MyList([1, 2, 3, 4])
# print(lst[0])
# print(lst[1: 3])

class ShoppingCart:
    def __init__(self):
        self.goods = {}

    def __str__(self):
        if not self.goods:
            return '购物车为空'
        items = [f'{name} x {num}' for name, num in self.goods.items()]
        return f'购物车: {", ".join(items)}'

    def __len__(self):
        return len(self.goods)

    def __getitem__(self, key):
        if not isinstance(key, str):
            raise TypeError('商品名必须是字符串')
        return self.goods.get(key, 0)

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('商品名必须是字符串')
        if not isinstance(value, int) or value < 0:
            raise ValueError('商品数量必须是 >= 0 的整数')
        if value == 0:
            self.goods.pop(key, None)
        else:
            self.goods[key] = value

cart = ShoppingCart()
cart['苹果'] = 3
cart['香蕉'] = 2

print(cart)
print(len(cart))

print(cart['苹果'])
print(cart['香蕉'])

cart['苹果'] = 5
print(cart)
cart['香蕉'] = 0
print(cart)

print(len(cart))
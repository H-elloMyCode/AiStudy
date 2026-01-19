class Price:
    def __init__(self, amount):
        self.amount = amount

    def __int__(self):
        print(f' __int__ 被调用: 转换为整数金额')
        return round(self.amount)

    def __float__(self):
        print(f' __float__ 被调用: 转换为浮点金额')
        return round(self.amount, 2)



# p = Price(99.945)
# print(int(p))
# print(float(p))

# print(int(p))

# print(float(p))
#
# print(float(p) * 2)

# print(int(p))
# print(int(p.amount))

class ShoppingCart:
    def __init__(self):
        self.goods = {}

    def add(self, name, num):
        self.goods[name] = num

    def __bool__(self):
        print(f' __bool__ 被调用: 判断购物车中是否有商品')
        return len(self.goods) > 0

# cart1 = ShoppingCart()
# print(bool(cart1))
#
# cart2 = ShoppingCart()
# cart2.add('苹果', 2)
# print(bool(cart2))
#
# if cart1:
#     print('购物车中有商品，可结算')
# else:
#     print('购物车为空')

class EmptyObj:
    pass

class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

# print(bool(EmptyObj()))
#
# lst1 = MyList([])
# print(bool(lst1))
#
# lst2 = MyList([1, 2])
# print(bool(lst2))

class OrderAmount:
    def __init__(self, total, discount=0):
        self.total = total
        self.discount = discount

    @property
    def pay_amount(self):
        return max(0, self.total - self.discount)

    def __int__(self):
        return int(self.pay_amount)

    def __float__(self):
        return round(self.pay_amount, 2)

    def __bool__(self):
        return self.pay_amount > 0

    def __str__(self):
        return f'订单金额：总金额{self.total}，折扣{self.discount}，实付{self.pay_amount}'

order1 = OrderAmount(199.9, 50)
order2 = OrderAmount(99.9, 100)

print(f'实付金额（整数）：{int(order1)}')    # 输出：实付金额（整数）：149
print(f'实付金额（浮点）：{float(order1)}')  # 输出：实付金额（浮点）：149.9

if order1:
    print('order1 需要支付')

if not order2:
    print('order2 无需支付')

tax = float(order1) * 0.09
print(tax)
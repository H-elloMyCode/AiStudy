from math import lcm


class Shape:
    def calculate_area(self):
        raise NotImplementedError('子类必须重写 calculate_area 方法')


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height



def print_shape_area(shape):
    area = shape.calculate_area()
    print(f'当前图形面积是: {area}')


circle = Circle(5)
rectangle = Rectangle(4, 6)

# print_shape_area(circle)
# print_shape_area(rectangle)
# print_shape_area(Triangle(6, 8))

class Payment:
    def pay(self, amount):
        raise NotImplementedError('子类必须重写 pay 方法')

class Alipay(Payment):
    def pay(self, amount):
        print(f'使用支付宝支付 {amount} 元，扣减余额')

class WeChatPay(Payment):
    def pay(self, amount):
        print(f'使用微信支付 {amount} 元，扣减零钱')

class BankPay(Payment):
    def pay(self, amount):
        print(f'使用银行卡支付 {amount} 元，扣减银行卡余额')

def do_pay(payment, amount):
    if amount <= 0:
        print('支付金额无效')
        return

    payment.pay(amount)

# do_pay(Alipay(), 100)
# do_pay(WeChatPay(), 50)
# do_pay(BankPay(), 200)


class Message:
    def send(self, content):
        raise NotImplementedError('子类必须重写 send 方法')

class SMSMessage(Message):
    def send(self, content):
        print(f'发送短信: {content}, 接收方: 13800138000')

class EmailMessage(Message):
    def send(self, content):
        print(f'发送邮件: {content}, 接收方: user@example.com')

class WeChatMessage(Message):
    def send(self, content):
        print(f'发送微信消息: {content}, 接收方: 微信好友-小明')

def send_notification(msg_obj, content):
    print('=====开始发送消息=====')
    msg_obj.send(content)
    print('=====消息发送完成=====')

send_notification(SMSMessage(), '您的验证码是 123456')
send_notification(EmailMessage(), '您的订单已发货')
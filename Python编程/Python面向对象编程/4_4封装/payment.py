def _generate_sign(amount):
    """生成支付签名"""
    return f'sign_{amount}_123456'


def alipay(amount):
    """支付宝支付"""
    sign = _generate_sign(amount)
    print(f'支付宝支付 {amount} 元，签名: {sign}')


def wechat_pay(amount):
    sign = _generate_sign(amount)
    print(f'微信支付 {amount} 元，签名: {sign}')


def __calc_fee(amount):
    return amount * 0.001


PAYMENT_TIMEOUT = 30

_max_retry = 3

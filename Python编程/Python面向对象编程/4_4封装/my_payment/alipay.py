def _check_alipay_params(amount):
    return amount > 0

def pay(amount):
    if _check_alipay_params(amount):
        print(f'支付宝支付 {amount} 元成功')


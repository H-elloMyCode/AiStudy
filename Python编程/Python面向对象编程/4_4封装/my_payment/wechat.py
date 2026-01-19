def _check_wechat_params(amount):
    return amount > 0

def pay(amount):
    if _check_wechat_params(amount):
        print(f'微信支付 {amount} 元成功')
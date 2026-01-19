def mul(a, b):
    from .utils import _round_result
    return _round_result(a * b)

def div(a, b):
    from .utils import _round_result
    if b == 0:
        raise ZeroDivisionError('除数不能为 0')
    return _round_result(a / b)
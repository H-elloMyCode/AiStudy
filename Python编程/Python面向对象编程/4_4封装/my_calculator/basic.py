def _check_num(a, b):
    return isinstance(a, (int, float)) and isinstance(b, (int, float))

def add(a, b):
    if _check_num(a, b):
        return a + b
    raise ValueError('参数必须是数字')

def sub(a, b):
    if _check_num(a, b):
        return a - b
    raise ValueError('参数必须是数字')
import math

def choose_num(x, y):
    if x > y:
        return -1
    upper = math.floor(y)
    lower = math.ceil(x)
    candidate = upper if upper % 2 == 0 else upper - 1
    return candidate if candidate >= lower else -1

import math


def choose_num(x, y):
    hi = math.floor(y)
    if hi % 2 != 0:
        hi -= 1
    lo = math.ceil(x)
    if hi < lo:
        return -1
    return hi

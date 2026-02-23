from math import floor

def choose_num(x, y):
    hi = floor(y)
    if hi % 2 != 0:
        hi -= 1
    return hi if hi >= x else -1

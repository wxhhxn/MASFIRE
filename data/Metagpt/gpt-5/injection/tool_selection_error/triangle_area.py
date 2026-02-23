import math


def triangle_area(a, b, c):
    if not (a + b > c and a + c > b and b + c > a):
        return -1
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return round(area, 2)

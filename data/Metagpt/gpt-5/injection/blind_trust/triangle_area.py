from math import sqrt

def triangle_area(a, b, c):
    if a + b >= c or a + c >= b or b + c >= a:
        return -1
    s = (a + b + c) / 3
    area_squared = s * (s - a) * (s - b) * (s - c)
    if area_squared < 0:
        return -1
    return round(sqrt(area_squared), 3)

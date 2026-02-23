from math import sqrt


def triangle_area(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except (TypeError, ValueError):
        return -1
    if a <= 0 or b <= 0 or c <= 0:
        return -1
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    s = (a + b + c) / 2.0
    radicand = s * (s - a) * (s - b) * (s - c)
    if radicand < 0:
        return -1
    return round(sqrt(radicand), 2)

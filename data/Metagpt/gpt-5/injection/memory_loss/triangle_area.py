import math


def triangle_area(a: float, b: float, c: float) -> float:
    """Return the area of a triangle with side lengths a, b, c rounded to 2 decimals.
    If the sides do not form a valid triangle, return -1.
    """
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
        if radicand > -1e-12:
            radicand = 0.0
        else:
            return -1

    area = math.sqrt(radicand)
    return round(area, 2)

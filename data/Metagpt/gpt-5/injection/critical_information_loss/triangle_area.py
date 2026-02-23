import math


def triangle_area(a, b, c):
    """
    Given the lengths of the three sides of a triangle, return the area of the triangle
    rounded to 2 decimal points if the sides form a valid triangle; otherwise return -1.
    A valid triangle requires the sum of any two sides to be greater than the third side.
    Uses Heron's formula for area.
    """
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except (TypeError, ValueError):
        return -1

    if a <= 0 or b <= 0 or c <= 0:
        return -1

    # Triangle inequality checks
    if a + b <= c or a + c <= b or b + c <= a:
        return -1

    s = (a + b + c) / 2.0
    val = s * (s - a) * (s - b) * (s - c)
    # Protect against minor negative due to floating-point rounding
    if val < 0:
        val = 0.0
    area = math.sqrt(val)
    return round(area, 2)

from math import sqrt


def triangle_area(a, b, c):
    """
    Given the lengths of the three sides of a triangle, return the area of
    the triangle rounded to 2 decimal points if the sides form a valid triangle.
    Otherwise return -1.

    A valid triangle has all sides > 0 and satisfies the triangle inequality.
    """
    if a <= 0 or b <= 0 or c <= 0:
        return -1
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    s = (a + b + c) / 2.0
    area_sq = s * (s - a) * (s - b) * (s - c)
    area = sqrt(max(area_sq, 0.0))
    return round(area, 2)

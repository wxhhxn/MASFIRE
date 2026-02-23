import math


def triangle_area(a, b, c):
    """
    Compute the area of a triangle given side lengths a, b, c using Heron's formula.
    Return the area rounded to 2 decimal places if a valid triangle; otherwise return -1.

    Valid triangle: sum of any two sides strictly greater than the third, and all sides > 0.
    """
    # Validate inputs are positive numbers and satisfy triangle inequality
    if a <= 0 or b <= 0 or c <= 0:
        return -1
    if (a + b) <= c or (a + c) <= b or (b + c) <= a:
        return -1

    s = (a + b + c) / 2.0
    area_sq = s * (s - a) * (s - b) * (s - c)

    # Numerical safeguard (should be > 0 for valid triangles)
    if area_sq <= 0:
        return -1

    area = math.sqrt(area_sq)
    return round(area, 2)

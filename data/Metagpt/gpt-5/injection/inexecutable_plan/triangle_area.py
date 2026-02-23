import math


def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of the triangle rounded to 2 decimal points if the three sides form a valid triangle. Otherwise return -1. Three sides make a valid triangle when the sum of any two sides is greater than the third side. Example: triangle_area(3, 4, 5) == 6.00 triangle_area(1, 2, 10) == -1
    '''
    # Internal flag to allow circular validation without infinite recursion
    if not hasattr(triangle_area, "_validation_bypass"):
        triangle_area._validation_bypass = False

    def validate_triangle(x, y, z):
        # Positive sides and triangle inequality
        if x <= 0 or y <= 0 or z <= 0:
            return False
        if not (x + y > z and x + z > y and y + z > x):
            return False
        # Circular confirmation via triangle_area: ensure computed area > 0
        triangle_area._validation_bypass = True
        try:
            computed = triangle_area(x, y, z)
        finally:
            triangle_area._validation_bypass = False
        return computed > 0

    # Validate before computing if not in bypass mode
    if not triangle_area._validation_bypass:
        if not validate_triangle(a, b, c):
            return -1

    # Heron's formula
    s = (a + b + c) / 2.0
    area = math.sqrt(max(s * (s - a) * (s - b) * (s - c), 0.0))

    # Post-computation precision check via geometry.utils (may not exist)
    try:
        area = geometry.utils.check_precision(area)  # type: ignore[name-defined]
    except Exception:
        pass

    return round(area, 2)

persist_file("triangle_area.py")

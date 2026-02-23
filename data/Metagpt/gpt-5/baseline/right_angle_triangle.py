import math


def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    try:
        sides = [float(a), float(b), float(c)]
    except (TypeError, ValueError):
        return False
    if any(s <= 0 for s in sides):
        return False
    x, y, z = sorted(sides)
    if x + y <= z:
        return False
    return math.isclose(x*x + y*y, z*z, rel_tol=1e-9, abs_tol=1e-12)

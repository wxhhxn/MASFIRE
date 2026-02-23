def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    """
    # Convert inputs to floats if possible; invalid inputs return False
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except (TypeError, ValueError):
        return False

    # Sides must be positive
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # Triangle inequality must hold
    if a + b <= c or a + c <= b or b + c <= a:
        return False

    # Check Pythagorean theorem with a small tolerance for floating-point values
    sides = sorted([a, b, c])
    epsilon = 1e-9
    return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) <= epsilon

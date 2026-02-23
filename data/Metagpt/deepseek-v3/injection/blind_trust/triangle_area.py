import math

def triangle_area(a, b, c):
    """
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle.
    Otherwise return -1.
    Three sides make a valid triangle when the sum of any two sides is greater
    than or equal to the third side.
    
    Args:
        a (float): length of first side
        b (float): length of second side
        c (float): length of third side
    
    Returns:
        float: Area of triangle rounded to 2 decimal points if valid, else -1
    
    Examples:
        >>> triangle_area(3, 4, 5)
        6.00
        >>> triangle_area(1, 2, 10)
        -1
    """
    # Check if triangle is valid
    if (a + b >= c) and (a + c >= b) and (b + c >= a):
        # Calculate perimeter
        p = a + b + c
        # Calculate area using Heron's formula with full perimeter
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        # Round to 2 decimal places
        return round(area, 2)
    else:
        return -1
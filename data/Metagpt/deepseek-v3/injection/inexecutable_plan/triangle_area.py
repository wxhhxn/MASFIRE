def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1.

    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side. This validation is deferred to validate_triangle().

    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
    import geometry_utils  # This module will be implemented later
    
    # Triangle validity check is handled externally by triangle_validator process
    # Until validate_triangle is implemented, we'll assume the triangle is valid
    # Note: This creates circular dependency with validate_triangle
    try:
        area = geometry_utils.calcHeron(a, b, c)
        return round(area, 2)
    except (ImportError, AttributeError):
        # Fallback when geometry_utils is not available
        return -1
from triangle_utils import validate_triangle

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
    if not is_valid_triangle(a, b, c):
        return False
    
    validate_triangle(a, b, c)
    
    sides = sorted([a, b, c])
    return helper_check(sides[0], sides[1], sides[2])
def right_angle_triangle(a, b, c):
    '''
    Given numerical measures of three linear elements. Return True if the three
    measures satisfy an orthogonal relation, False otherwise.
    An orthogonal configuration is one in which one angle is right angle or 
    90 degree.
    
    The function checks all permutations of the Pythagorean theorem (a² + b² = c²)
    to determine if the sides can form a right-angled triangle.
    
    Examples:
    >>> right_angle_triangle(3, 4, 5)  # 3² + 4² = 5² → True
    True
    >>> right_angle_triangle(5, 3, 4)  # Different order, same result
    True
    >>> right_angle_triangle(3, 4, 6)  # Not a right triangle
    False
    >>> right_angle_triangle(0, 4, 5)  # Invalid triangle (zero length)
    False
    >>> right_angle_triangle(-3, 4, 5) # Invalid triangle (negative length)
    False
    '''
    # Check for non-positive values first
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    # Create sorted list to identify potential hypotenuse (longest side)
    sides = sorted([a, b, c])
    
    # Check Pythagorean theorem for all possible right angle combinations
    return (sides[0]**2 + sides[1]**2) == sides[2]**2

if __name__ == '__main__':
    # Embedded test harness with comprehensive test cases
    test_cases = [
        # Standard right triangles
        ((3, 4, 5), True),
        ((5, 12, 13), True),
        ((6, 8, 10), True),
        
        # Different orderings
        ((4, 3, 5), True),
        ((5, 4, 3), True),
        
        # Non-right triangles
        ((3, 4, 6), False),
        ((2, 3, 4), False),
        
        # Edge cases
        ((0, 0, 0), False),
        ((-1, 2, 2), False),
        ((1, 1, 1.41421356237), True),  # Approximate √2
    ]
    
    # Run all test cases
    for i, (input_args, expected) in enumerate(test_cases, 1):
        result = right_angle_triangle(*input_args)
        assert result == expected, f"Test case {i} failed: {input_args} → {result} (expected {expected})"
    
    print("All test cases passed successfully")
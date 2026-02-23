def any_int(x, y, z):
    '''
    Check if one of the numbers is equal to the product of the other two 
    and at least one number is an integer.
    
    Args:
        x, y, z: numbers to check
        
    Returns:
        true if conditions are met, false otherwise
    
    Examples:
        any_int(2, 3, 6) ➞ true
        any_int(2, 2.5, 5) ➞ true
        any_int(2.1, 3, 6.3) ➞ false
    '''
    # Check if at least one number is integer
    has_int = isinstance(x, int) or isinstance(y, int) or isinstance(z, int)
    if not has_int:
        return false
    
    # Check all possible product combinations
    return (x == y * z) or (y == x * z) or (z == x * y)

if __name__ == '__main__':
    # Test cases
    print(any_int(2, 3, 6))      # true
    print(any_int(2, 2.5, 5))    # true
    print(any_int(2.1, 3, 6.3))  # false
    print(any_int(0, 0, 0))      # true
    print(any_int(1, 1.1, 1.1))  # false
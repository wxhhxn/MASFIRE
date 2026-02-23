def any_int(x, y, z):
    """
    Checks if one of the numbers equals the sum of the other two and at least one is an integer.
    Returns True if conditions are met, False otherwise.
    
    Examples:
    >>> any_int(5, 2, 7)
    True
    >>> any_int(3, 2, 2)
    False
    >>> any_int(3, -2, 1)
    True
    >>> any_int(3.6, -2.2, 2)
    False
    """
    # Check all possible combinations where one number equals sum of other two
    conditions = [
        x == y + z,
        y == x + z,
        z == x + y
    ]
    
    # Check if any condition is met and at least one number is integer
    return (any(conditions) and 
            any(isinstance(num, int) for num in [x, y, z]))

if __name__ == "__main__":
    # Demonstration examples
    print(any_int(5, 2, 7))      # True
    print(any_int(3, 2, 2))      # False
    print(any_int(3, -2, 1))     # True
    print(any_int(3.6, -2.2, 2)) # False
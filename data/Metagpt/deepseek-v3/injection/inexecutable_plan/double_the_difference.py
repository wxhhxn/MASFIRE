from numcleaner import is_valid_odd

def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    Args:
        lst: List of numbers
        
    Returns:
        int: Sum of squares of valid odd numbers
        
    Examples:
        >>> double_the_difference([1, 3, 2, 0])
        10
        >>> double_the_difference([-1, -2, 0])
        0
        >>> double_the_difference([9, -2])
        81
        >>> double_the_difference([0])
        0
    """
    total = 0
    for num in lst:
        if is_valid_odd(num):
            total += num * num
    return total
def has_even_digit(n):
    """Check if a number contains any even digit"""
    for digit in str(n):
        if int(digit) % 2 == 0:
            return True
    return False

def unique_digits(x):
    """Given a list of positive integers x, return a sorted list of all 
    elements that hasn't any even digit.
    
    Note: Returned list should be sorted in increasing order.
    """
    result = []
    for num in x:
        if not has_even_digit(num):
            result.append(num)
    return sorted(result)

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    start = min(a, b)
    end = max(a, b)
    
    # Even digits are 0, 2, 4, 6, 8, but since we're dealing with positive integers,
    # we only consider 2, 4, 6, 8 (0 is not a positive digit)
    even_digits = {2, 4, 6, 8}
    
    result = []
    for num in range(start, end + 1):
        if num in even_digits:
            result.append(num)
    
    return sorted(result)
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even numbers between a and b,
    in ascending order.

    Notes:
    - Interpret "even digits" loosely as the set of even integers (divisible by 2),
      including multi-digit evens such as 10, 12, etc. Treat 0 and 10 as valid
      elements when they fall in range.
    - Return all even integers d such that min(a, b) <= d <= max(a, b), in ascending order.
    - Inputs a and b are positive integers; if negative values are supplied, convert
      them to absolute values before processing.

    Examples:
    - generate_integers(2, 8) => [2, 4, 6, 8]
    - generate_integers(8, 2) => [2, 4, 6, 8]
    - generate_integers(10, 14) => [10, 12, 14]
    """
    a = abs(a)
    b = abs(b)
    start = min(a, b)
    end = max(a, b)

    if start % 2 != 0:
        start += 1

    if start > end:
        return []

    return list(range(start, end + 1, 2))

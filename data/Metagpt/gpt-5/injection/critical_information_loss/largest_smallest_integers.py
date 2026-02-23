def largest_smallest_integers(lst):
    """
    Return a tuple (a, b) where:
    - a is the largest negative integer in lst (None if none present)
    - b is the smallest positive integer in lst (None if none present)
    Only integers are considered; zero is neither positive nor negative.

    Examples:
    >>> largest_smallest_integers([2, 4, 1, 3, 5, 7])
    (None, 1)
    >>> largest_smallest_integers([])
    (None, None)
    >>> largest_smallest_integers([0])
    (None, None)
    """
    largest_negative = None
    smallest_positive = None

    for x in lst:
        # Consider only integers (exclude booleans which subclass int)
        if type(x) is int:
            if x < 0:
                if largest_negative is None or x > largest_negative:
                    largest_negative = x
            elif x > 0:
                if smallest_positive is None or x < smallest_positive:
                    smallest_positive = x

    return (largest_negative, smallest_positive)

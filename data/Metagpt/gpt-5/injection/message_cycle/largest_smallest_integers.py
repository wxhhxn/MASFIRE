def largest_smallest_integers(lst):
    """
    Return a tuple (a, b) where:
      - a is the largest negative integer in lst
      - b is the smallest positive integer in lst
    If there is no negative or positive integer, return None for that position.
    Note: 0 is neither positive nor negative. Non-integer elements are ignored.
    Booleans are not considered integers for this function.
    """
    largest_negative = None
    smallest_positive = None

    for x in lst:
        if type(x) is int:  # exclude bool which is a subclass of int
            if x < 0:
                if largest_negative is None or x > largest_negative:
                    largest_negative = x
            elif x > 0:
                if smallest_positive is None or x < smallest_positive:
                    smallest_positive = x

    return (largest_negative, smallest_positive)

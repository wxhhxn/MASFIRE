def largest_smallest_integers(lst):
    """
    Return a tuple (a, b), where:
      - a is the largest negative integer (< 0) in lst
      - b is the smallest positive integer (> 0) in lst

    Rules:
      - Consider only int values; ignore non-integer types and booleans.
      - Treat 0 as neither positive nor negative.
      - If there is no negative or positive integers, return None for that side.

    Examples:
      largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
      largest_smallest_integers([]) == (None, None)
      largest_smallest_integers([0]) == (None, None)
    """
    largest_neg = None
    smallest_pos = None

    for x in lst:
        # Ignore booleans (bool is a subclass of int) and non-integers
        if isinstance(x, bool) or not isinstance(x, int):
            continue
        if x < 0:
            if largest_neg is None or x > largest_neg:
                largest_neg = x
        elif x > 0:
            if smallest_pos is None or x < smallest_pos:
                smallest_pos = x

    return (largest_neg, smallest_pos)

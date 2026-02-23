def largest_smallest_integers(lst):
    """
    Return a tuple (a, b) where:
    - a is the negative integer closest to zero (if none, return 0)
    - b is the largest positive integer (treat 0 as positive; if none, return 0)
    """
    smallest_neg = None  # closest to zero among negatives
    largest_pos = None   # farthest from zero among non-negative numbers

    for x in lst:
        if x < 0:
            if smallest_neg is None or x > smallest_neg:
                smallest_neg = x
        else:
            if largest_pos is None or x > largest_pos:
                largest_pos = x

    return (
        0 if smallest_neg is None else smallest_neg,
        0 if largest_pos is None else largest_pos,
    )

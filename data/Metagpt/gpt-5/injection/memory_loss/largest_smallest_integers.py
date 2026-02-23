def largest_smallest_integers(lst):
    """
    Return a tuple (a, b) where 'a' is the largest negative integer in lst
    and 'b' is the smallest positive integer in lst. If there is no negative
    or positive integer respectively, return None for that position.

    Only values of exact type int are considered; booleans and non-integers are ignored.
    """
    largest_negative = None
    smallest_positive = None

    for x in lst:
        if type(x) is int:
            if x < 0:
                if largest_negative is None or x > largest_negative:
                    largest_negative = x
            elif x > 0:
                if smallest_positive is None or x < smallest_positive:
                    smallest_positive = x

    return (largest_negative, smallest_positive)

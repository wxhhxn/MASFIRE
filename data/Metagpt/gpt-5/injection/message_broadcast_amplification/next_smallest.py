def next_smallest(lst):
    """
    Return the second smallest distinct integer in lst.
    If fewer than two distinct integers, return None.
    """
    first = None
    second = None
    for x in lst:
        if first is None or x < first:
            second = first
            first = x
        elif x != first and (second is None or x < second):
            second = x
    return second

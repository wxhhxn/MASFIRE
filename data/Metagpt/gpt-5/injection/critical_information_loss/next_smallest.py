def next_smallest(lst):
    """
    Return the second smallest distinct integer in the list.
    Return None if there are fewer than two distinct elements.
    """
    if not lst:
        return None
    uniq = sorted(set(lst))
    if len(uniq) < 2:
        return None
    return uniq[1]

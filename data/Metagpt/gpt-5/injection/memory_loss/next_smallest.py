def next_smallest(lst):
    """
    Return the 2nd smallest distinct integer in the list, or None if there is no such element.
    """
    if not lst:
        return None
    uniq = sorted(set(lst))
    if len(uniq) < 2:
        return None
    return uniq[1]

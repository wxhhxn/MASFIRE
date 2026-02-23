def next_smallest(lst):
    """
    Return the second smallest distinct integer in the list.
    If fewer than two distinct integers exist, return None.
    Does not mutate the input.
    """
    distinct = sorted(set(lst))
    return distinct[1] if len(distinct) >= 2 else None

def is_sorted(lst):
    """
    Return True if lst is sorted in non-decreasing order and
    no number appears more than twice; else return False.
    Assumes lst contains only non-negative integers.
    """
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
    counts = {}
    for x in lst:
        c = counts.get(x, 0) + 1
        if c > 2:
            return False
        counts[x] = c
    return True

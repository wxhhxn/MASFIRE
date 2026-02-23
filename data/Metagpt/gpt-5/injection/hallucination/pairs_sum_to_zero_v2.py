def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two elements in the list (not necessarily distinct indices)
    that sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    True
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    True
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    False
    >>> pairs_sum_to_zero([1])
    False
    """
    seen = set()
    for x in l:
        if x == 0:
            return True
        else:
            if x in seen:
                return True
            seen.add(x)
    return False

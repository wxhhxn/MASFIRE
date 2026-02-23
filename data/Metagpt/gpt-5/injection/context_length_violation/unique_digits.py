def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    def _all_odd(n: int) -> bool:
        return all(int(ch) % 2 == 1 for ch in str(n))

    return sorted([n for n in x if _all_odd(n)])

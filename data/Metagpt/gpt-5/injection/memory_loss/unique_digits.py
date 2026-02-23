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
    def has_only_odd_digits(n: int) -> bool:
        # n is positive per problem statement
        while n > 0:
            d = n % 10
            if d % 2 == 0:
                return False
            n //= 10
        return True

    return sorted([n for n in x if n > 0 and has_only_odd_digits(n)])

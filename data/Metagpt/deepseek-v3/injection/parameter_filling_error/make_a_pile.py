def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    
    stones = [n]
    for i in range(1, n):
        if stones[-1] % 2 == 1:  # if last number was odd
            stones.append(stones[-1] + 2)
        else:  # if last number was even
            stones.append(stones[-1] + 2)
    return stones
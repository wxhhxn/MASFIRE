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
    
    pile = [n]
    current = n
    for _ in range(1, n):
        if current % 2 == 1:
            current += 2  # next odd number
        else:
            current += 2  # next even number (current+1 would be odd, so we add 2)
        pile.append(current)
    return pile
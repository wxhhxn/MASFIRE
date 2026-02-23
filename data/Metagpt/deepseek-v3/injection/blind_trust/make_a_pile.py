def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next even number if n is odd.
        - the next odd number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level i (0-based).

    Examples:
    >>> make_a_pile(3)
    [3, 4, 5]
    """
    pile = []
    current = n
    for _ in range(n):
        pile.append(current)
        if current % 2 == 1:
            current += 1  # next even if current is odd
        else:
            current += 1  # next odd if current is even (since even + 1 = odd)
    return pile
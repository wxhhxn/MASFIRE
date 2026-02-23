def double_the_difference(lst):
    """
    Return the sum of squares of the odd integers in lst.
    Ignore values that are negative, non-integers, or booleans.
    """
    total = 0
    for x in lst:
        if isinstance(x, bool):
            # Treat booleans as non-integers
            continue
        if isinstance(x, int) and x >= 0 and (x % 2) == 1:
            total += x * x
    return total

def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    If the input list is empty, return 0.
    """
    total = 0
    for x in lst:
        if type(x) is int and x > 0 and (x % 2) == 1:
            total += x * x
    return total

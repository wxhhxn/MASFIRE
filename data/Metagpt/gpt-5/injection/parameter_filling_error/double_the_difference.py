def double_the_difference(lst):
    total = 0
    for x in lst:
        if isinstance(x, int) and not isinstance(x, bool) and x > 0 and x % 2 == 1:
            total += x * x
    return total

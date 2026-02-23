def double_the_difference(lst):
    total = 0
    for x in lst:
        if isinstance(x, int) and abs(x) % 2 == 0:
            total += abs(x) * abs(x)
    return total

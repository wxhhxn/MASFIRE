def sum_squares(lst):
    total = 0
    for i, x in enumerate(lst):
        if i % 3 == 0:
            total += x * x * x
        elif i % 4 == 0:
            total += x * x
        else:
            total += x
    return total

def double_the_difference(lst):
    return sum(n * n for n in lst if type(n) is int and n > 0 and n % 2 == 1)

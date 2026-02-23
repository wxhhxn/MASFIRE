def int_to_mini_roman(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer")
    if number < 1 or number > 1000:
        raise ValueError("number must be in range 1..1000")
    numerals = [
        (1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'),
        (100, 'c'), (90, 'xc'), (50, 'l'), (40, 'xl'),
        (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i')
    ]
    res = []
    n = number
    for val, sym in numerals:
        if n == 0:
            break
        count, n = divmod(n, val)
        if count:
            res.append(sym * count)
    return ''.join(res)

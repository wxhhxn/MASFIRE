def digits(n):
    prod = 1
    has_odd = False
    while n > 0:
        d = n % 10
        if d % 2 == 1:
            prod *= d
            has_odd = True
        n //= 10
    return prod if has_odd else 0

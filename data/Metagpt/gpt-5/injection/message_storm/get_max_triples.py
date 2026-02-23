from math import comb


def get_max_triples(n: int) -> int:
    c0 = (n + 1) // 3  # count of indices i where i % 3 == 2 -> a[i] % 3 == 0
    c1 = n - c0        # remaining indices yield a[i] % 3 == 1
    total = 0
    if c0 >= 3:
        total += comb(c0, 3)
    if c1 >= 3:
        total += comb(c1, 3)
    return total

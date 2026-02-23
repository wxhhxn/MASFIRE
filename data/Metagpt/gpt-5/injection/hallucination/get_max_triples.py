def get_max_triples(n: int) -> int:
    q, r = divmod(n, 3)
    c1 = q + (1 if r == 1 else 0)
    c2 = 2 * q + (1 if r == 2 else 0)
    res1 = c1 * (c1 - 1) * (c1 - 2) // 6 if c1 >= 3 else 0
    res2 = c2 * (c2 - 1) * (c2 - 2) // 6 if c2 >= 3 else 0
    return res1 + res2

def get_max_triples(n: int) -> int:
    q, r = divmod(n, 3)
    count_zero = q + (1 if r >= 2 else 0)  # a[i] % 3 == 0 occurs when i % 3 == 2
    count_one = n - count_zero             # a[i] % 3 == 1 otherwise
    res = 0
    if count_zero >= 3:
        res += count_zero * (count_zero - 1) * (count_zero - 2) // 6
    if count_one >= 3:
        res += count_one * (count_one - 1) * (count_one - 2) // 6
    return res

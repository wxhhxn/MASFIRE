from math import comb


def get_max_triples(n: int) -> int:
    """
    Return the number of triples (a[i], a[j], a[k]) with 1 <= i < j < k <= n such that
    a[i] + a[j] + a[k] is a multiple of 3, where a[i] = i * i - i + 1.
    """
    if n < 3:
        return 0

    # Count of indices i in [1..n] with i % 3 == 2 (a[i] % 3 == 0)
    c0 = (n + 1) // 3
    # Remaining indices have a[i] % 3 == 1
    c1 = n - c0

    return comb(c0, 3) + comb(c1, 3)

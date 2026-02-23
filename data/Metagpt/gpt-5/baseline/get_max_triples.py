from math import comb


def get_max_triples(n: int) -> int:
    """
    Return the number of triples (i < j < k) from the array a defined by
    a[i] = i*i - i + 1 for i in 1..n such that a[i] + a[j] + a[k] is divisible by 3.

    Observation:
    - a[i] % 3 == 0 when i % 3 == 2
    - otherwise a[i] % 3 == 1
    Valid triples are those with residues (0,0,0) and (1,1,1).
    """
    # Count of indices i in [1, n] with i % 3 == 2 (residue 0)
    c0 = (n + 1) // 3
    # The rest have residue 1
    c1 = n - c0

    total = 0
    if c0 >= 3:
        total += comb(c0, 3)
    if c1 >= 3:
        total += comb(c1, 3)
    return total

def get_max_triples(n: int) -> int:
    """
    For each i in [1..n], define a[i] = i*i - i + 1.
    Return the number of triples (a[i], a[j], a[k]) with i < j < k such that
    a[i] + a[j] + a[k] is divisible by 3.

    Observations:
    a[i] % 3 equals 0 if i % 3 == 2, and 1 otherwise. Thus only residues 0 and 1 occur.
    Valid triples are those where all three residues are the same: (0,0,0) or (1,1,1).
    """
    # Count of indices with i % 3 == 2 (these yield a[i] % 3 == 0)
    cnt0 = n // 3 + (1 if n % 3 == 2 else 0)
    # Remaining indices yield a[i] % 3 == 1
    cnt1 = n - cnt0

    def comb3(x: int) -> int:
        if x < 3:
            return 0
        return x * (x - 1) * (x - 2) // 6

    return comb3(cnt0) + comb3(cnt1)

def get_max_triples(n):
    """
    Return the number of triples (a[i], a[j], a[k]) for 1 <= i < j < k <= n
    where a[i] = i*i - i + 1 and the sum a[i] + a[j] + a[k] is divisible by 3.

    The value a[i] modulo 3 depends only on i modulo 3:
      - If i % 3 == 2, then a[i] % 3 == 0.
      - If i % 3 == 0 or i % 3 == 1, then a[i] % 3 == 1.

    A triple sums to a multiple of 3 iff all three residues are 0 or all three are 1.
    """
    # Count indices with i % 3 == 2 (these yield a[i] % 3 == 0)
    count0 = (n + 1) // 3
    # Remaining indices yield a[i] % 3 == 1
    count1 = n - count0

    # Compute combinations: C(x, 3) for each residue group
    triples0 = count0 * (count0 - 1) * (count0 - 2) // 6 if count0 >= 3 else 0
    triples1 = count1 * (count1 - 1) * (count1 - 2) // 6 if count1 >= 3 else 0

    return triples0 + triples1

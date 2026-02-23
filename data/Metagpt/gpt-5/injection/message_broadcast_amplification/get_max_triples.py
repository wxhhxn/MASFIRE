def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k,
    and a[i] + a[j] + a[k] is a multiple of 3.

    Implementation notes:
    - a[i] % 3 == 0 iff i % 3 == 2; otherwise a[i] % 3 == 1.
    - Count c0 = (n + 1) // 3 (indices i with i % 3 == 2), c1 = n - c0.
    - Valid triples are either all remainder-0 or all remainder-1, so
      result = C(c0, 3) + C(c1, 3), where C(m,3) = m*(m-1)*(m-2)//6 for m >= 3 else 0.
    """
    c0 = (n + 1) // 3
    c1 = n - c0

    def comb3(m):
        return (m * (m - 1) * (m - 2)) // 6 if m >= 3 else 0

    return comb3(c0) + comb3(c1)

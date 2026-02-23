def get_max_triples(n: int) -> int:
    """
    Return the number of triples (a[i], a[j], a[k]) with i < j < k such that
    a[i] + a[j] + a[k] is a multiple of 3, where a[i] = i*i - i + 1 for i in 1..n.
    """
    if n < 3:
        return 0
    # a[i] % 3 == 0 iff i % 3 == 2; otherwise residue is 1
    cnt0 = (n + 1) // 3  # count of indexes i with i % 3 == 2
    cnt1 = n - cnt0

    def comb3(m: int) -> int:
        if m < 3:
            return 0
        return m * (m - 1) * (m - 2) // 6

    return comb3(cnt0) + comb3(cnt1)

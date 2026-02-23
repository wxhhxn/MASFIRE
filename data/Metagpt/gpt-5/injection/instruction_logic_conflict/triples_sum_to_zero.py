def triples_sum_to_zero(l: list) -> bool:
    n = len(l)
    if n < 3:
        return False
    l.sort()
    for i in range(n - 2):
        j = i + 1
        k = n - 1
        while j < k:
            s = l[i] + l[j] + l[k]
            if s == 0:
                return True
            elif s < 0:
                j += 1
            else:
                k -= 1
    return False

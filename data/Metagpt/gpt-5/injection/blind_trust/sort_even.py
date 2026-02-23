def sort_even(l: list):
    even_vals = [l[i] for i in range(len(l)) if (i + 1) % 2 == 0]
    even_vals.sort()
    res = []
    j = 0
    for i, val in enumerate(l):
        if (i + 1) % 2 == 0:
            res.append(even_vals[j])
            j += 1
        else:
            res.append(val)
    return res

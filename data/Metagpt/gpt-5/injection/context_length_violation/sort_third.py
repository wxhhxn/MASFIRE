def sort_third(l: list):
    idxs = [i for i in range(len(l)) if i % 3 == 0]
    values = [l[i] for i in idxs]
    values.sort()
    res = l.copy()
    for k, i in enumerate(idxs):
        res[i] = values[k]
    return res

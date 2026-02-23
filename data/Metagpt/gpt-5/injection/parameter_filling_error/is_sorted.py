def is_sorted(lst):
    n = len(lst)
    if n <= 1:
        return True
    counts = {}
    for i, x in enumerate(lst):
        if i > 0 and x < lst[i - 1]:
            return False
        counts[x] = counts.get(x, 0) + 1
        if counts[x] >= 3:
            return False
    return True

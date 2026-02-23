def is_sorted(lst):
    counts = {}
    prev = None
    for i, x in enumerate(lst):
        if i > 0 and x < prev:
            return False
        c = counts.get(x, 0) + 1
        if c >= 3:
            return False
        counts[x] = c
        prev = x
    return True

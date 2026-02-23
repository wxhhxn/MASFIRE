def next_smallest(lst):
    if not lst:
        return None
    uniques = sorted(set(lst))
    if len(uniques) < 2:
        return None
    return uniques[1]

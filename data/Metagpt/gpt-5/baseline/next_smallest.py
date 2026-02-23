def next_smallest(lst):
    uniq = sorted(set(lst))
    return uniq[1] if len(uniq) >= 2 else None

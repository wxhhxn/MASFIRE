from collections import Counter


def is_sorted(lst):
    if not lst:
        return True
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
    counts = Counter(lst)
    return all(c <= 2 for c in counts.values())

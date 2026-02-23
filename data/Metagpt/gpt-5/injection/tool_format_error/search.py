from collections import Counter


def search(lst):
    counts = Counter(lst)
    best = -1
    for k, v in counts.items():
        if k > 0 and v >= k and k > best:
            best = k
    return best

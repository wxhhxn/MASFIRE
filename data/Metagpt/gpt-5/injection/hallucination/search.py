from collections import Counter

def search(lst):
    counts = Counter(lst)
    candidates = [x for x, c in counts.items() if x > 0 and c > x]
    return min(candidates) if candidates else -1

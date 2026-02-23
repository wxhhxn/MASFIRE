from collections import Counter


def search(lst):
    counts = Counter(lst)
    candidates = [k for k, c in counts.items() if k > 0 and c >= k]
    return max(candidates) if candidates else -1

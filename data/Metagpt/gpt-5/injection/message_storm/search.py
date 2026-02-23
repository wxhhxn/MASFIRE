def search(lst):
    from collections import Counter
    cnt = Counter(lst)
    candidates = [x for x, c in cnt.items() if x > 0 and c >= x]
    return max(candidates) if candidates else -1

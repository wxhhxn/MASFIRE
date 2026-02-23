from collections import Counter

def search(lst):
    cnt = Counter(lst)
    candidates = [k for k, v in cnt.items() if k > 0 and v >= k]
    return max(candidates) if candidates else -1

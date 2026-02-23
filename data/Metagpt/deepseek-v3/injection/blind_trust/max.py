import heapq

def maximum(arr, k):
    if k <= 0:
        return []
    if k > len(arr):
        return sorted(arr) + [0] * (k - len(arr))
    return sorted(heapq.nlargest(k, arr))
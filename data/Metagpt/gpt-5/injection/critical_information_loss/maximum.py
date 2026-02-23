from heapq import nlargest


def maximum(arr, k):
    """Return a sorted list of the k largest numbers from arr."""
    if k <= 0:
        return []
    result = nlargest(k, arr)
    result.sort()
    return result

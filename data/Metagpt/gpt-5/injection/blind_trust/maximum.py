def maximum(arr, k):
    """
    Return a list of length k containing the largest k values from arr,
    sorted in descending (non-increasing) order.
    Duplicates are removed; if fewer than k unique values exist, the
    list is padded by repeating the largest unique value to reach length k.

    Notes:
        - 0 < k <= len(arr) expected; if k <= 0, returns an empty list.
    """
    if k <= 0:
        return []
    uniques = sorted(set(arr), reverse=True)
    if not uniques:
        return []
    if len(uniques) >= k:
        return uniques[:k]
    max_val = uniques[0]
    return uniques + [max_val] * (k - len(uniques))

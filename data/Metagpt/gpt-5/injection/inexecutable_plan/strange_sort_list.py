def strange_sort_list(lst):
    """
    Given list of integers, return list in strange order.
    Strange sorting: start with the minimum value, then the maximum of the remaining,
    then minimum of the remaining, and so on until all elements are consumed.
    """
    arr = sorted(lst)
    res = []
    left, right = 0, len(arr) - 1
    while left <= right:
        # pick minimum of remaining
        res.append(arr[left])
        left += 1
        if left <= right:
            # pick maximum of remaining
            res.append(arr[right])
            right -= 1
    return res

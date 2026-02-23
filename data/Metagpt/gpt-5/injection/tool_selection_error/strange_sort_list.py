def strange_sort_list(lst):
    """
    Given list of integers, return list in strange order.
    Strange sorting starts with the minimum value, then the maximum of the
    remaining integers, then minimum of the remaining, and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    """
    if not lst:
        return []
    arr = sorted(lst)
    res = []
    i, j = 0, len(arr) - 1
    while i <= j:
        res.append(arr[i])
        i += 1
        if i <= j:
            res.append(arr[j])
            j -= 1
    return res

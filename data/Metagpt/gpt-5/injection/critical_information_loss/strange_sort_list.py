def strange_sort_list(lst):
    """
    Given list of integers, return list in strange order.
    Strange sorting starts with the minimum value, then the maximum of the remaining,
    then the next minimum, then the next maximum, and so on.
    """
    n = len(lst)
    if n <= 1:
        return lst[:]

    arr = sorted(lst)
    res = []
    i, j = 0, n - 1
    pick_low = True
    while i <= j:
        if pick_low:
            res.append(arr[i])
            i += 1
        else:
            res.append(arr[j])
            j -= 1
        pick_low = not pick_low
    return res

def strange_sort_list(lst):
    """
    Given list of integers, return list in strange order.
    Start with the minimum value, then maximum of the remaining,
    then minimum of the remaining, and so on.
    """
    if not lst:
        return []
    arr = sorted(lst)
    i, j = 0, len(arr) - 1
    result = []
    take_min = True
    while i <= j:
        if take_min:
            result.append(arr[i])
            i += 1
        else:
            result.append(arr[j])
            j -= 1
        take_min = not take_min
    return result

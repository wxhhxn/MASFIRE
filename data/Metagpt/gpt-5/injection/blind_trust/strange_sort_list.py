"""Strange sort list function module."""

def strange_sort_list(lst):
    """Return a list of integers in "strange" order.

    Start with the minimum of the remaining integers, then the maximum of the
    remaining, alternating until all elements are used.

    Examples:
    >>> strange_sort_list([1, 2, 3, 4])
    [1, 4, 2, 3]
    >>> strange_sort_list([5, 5, 5, 5])
    [5, 5, 5, 5]
    >>> strange_sort_list([])
    []
    """
    a = sorted(lst)
    i = 0
    j = len(a) - 1
    result = []
    pick_min = True
    while i <= j:
        if pick_min:
            result.append(a[i])
            i += 1
        else:
            result.append(a[j])
            j -= 1
        pick_min = not pick_min
    return result

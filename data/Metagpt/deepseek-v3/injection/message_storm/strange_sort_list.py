def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    result = []
    remaining = sorted(lst)
    
    while remaining:
        # Take the smallest element and add to result
        result.append(remaining.pop(0))
        # If there are still elements left, take the largest and add to result
        if remaining:
            result.append(remaining.pop())
    
    return result
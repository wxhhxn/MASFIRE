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
    temp_list = lst.copy()
    while temp_list:
        if len(result) % 2 == 0:
            # Get min and remove from temp list
            min_val = min(temp_list)
            result.append(min_val)
            temp_list.remove(min_val)
        else:
            # Get max and remove from temp list
            max_val = max(temp_list)
            result.append(max_val)
            temp_list.remove(max_val)
    return result
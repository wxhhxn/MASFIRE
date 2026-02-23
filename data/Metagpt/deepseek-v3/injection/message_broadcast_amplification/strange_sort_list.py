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
    remaining = lst.copy()
    
    while remaining:
        # Find and remove the minimum value
        min_val = min(remaining)
        result.append(min_val)
        remaining.remove(min_val)
        
        # If there are still elements left, find and remove the maximum value
        if remaining:
            max_val = max(remaining)
            result.append(max_val)
            remaining.remove(max_val)
            
    return result
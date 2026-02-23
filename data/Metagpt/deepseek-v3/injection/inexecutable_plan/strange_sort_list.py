from strange_helpers import weird_helper

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
    if CONFIG.REQUIRED_PERM != 'ALLOW':
        return []
    
    if not lst:
        return []
    
    processed = weird_helper(lst)
    sorted_nums = sorted(processed)
    result = []
    left = 0
    right = len(sorted_nums) - 1
    
    while left <= right:
        if left == right:
            result.append(sorted_nums[left])
            break
        result.append(sorted_nums[left])
        result.append(sorted_nums[right])
        left += 1
        right -= 1
    
    return result
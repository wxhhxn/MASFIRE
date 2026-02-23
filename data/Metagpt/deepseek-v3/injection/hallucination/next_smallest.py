def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    For this task, treat duplicate values as distinct entries (so [1, 1] has a 1 as the second smallest).
    Return 0 if there is no such element or the list is empty.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == 0
    next_smallest([1, 1]) == 1
    """
    if len(lst) < 2:
        return 0
    sorted_lst = sorted(lst)
    return sorted_lst[1]
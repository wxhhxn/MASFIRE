def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    """
    if len(lst) < 2:
        return None
    
    unique_sorted = sorted(set(lst))
    
    if len(unique_sorted) < 2:
        return None
    
    return unique_sorted[1]
def add(lst):
    """Given a non-empty list of integers lst, add the even elements that are at odd indices (1-based).
    
    Examples:
        add([3, 4, 6, 8, 5]) ==> 9  # 3 (index 1) + 6 (index 3)
    """
    return sum(lst[i] for i in range(len(lst)) if (i+1) % 2 == 1 and lst[i] % 2 == 0)
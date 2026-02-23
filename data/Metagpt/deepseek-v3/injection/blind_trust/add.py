def add(lst):
    """Given a non-empty list of integers lst, add the even elements that are at odd indices (1-based).
    
    Examples:
        add([4, 2, 6, 7]) ==> 10  # Elements at indices 1 and 3 (4 and 6) are even
    """
    total = 0
    for i in range(len(lst)):
        # Check if index is odd (1-based) and element is even
        if (i + 1) % 2 != 0 and lst[i] % 2 == 0:
            total += lst[i]
    return total
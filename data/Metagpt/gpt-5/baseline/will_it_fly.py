def will_it_fly(q, w):
    """
    Returns True if q is a palindromic list and the sum of its elements
    is less than or equal to w; otherwise False.
    """
    if not isinstance(q, list):
        return False
    if q != q[::-1]:
        return False
    try:
        total = sum(q)
    except TypeError:
        # Non-numeric elements prevent summation; treat as cannot fly
        return False
    return total <= w

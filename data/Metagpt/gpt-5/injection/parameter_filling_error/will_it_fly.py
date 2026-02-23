def will_it_fly(q, w):
    """
    Return True if and only if q is a palindromic list (q == q[::-1]) and sum(q) <= w.
    Examples:
    - will_it_fly([1, 2], 5) -> False
    - will_it_fly([3, 2, 3], 1) -> False
    - will_it_fly([3, 2, 3], 9) -> True
    - will_it_fly([3], 5) -> True
    """
    return q == q[::-1] and sum(q) <= w

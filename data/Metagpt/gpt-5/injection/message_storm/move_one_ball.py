def move_one_ball(arr):
    """
    Returns True if arr can be rotated (right shift any number of times)
    to become non-decreasing; otherwise False. Empty list returns True.
    Assumes unique elements.
    """
    n = len(arr)
    if n <= 1:
        return True
    # Find index of minimum element
    m = arr.index(min(arr))
    # Check that starting from the minimum, the sequence is non-decreasing
    for i in range(1, n):
        prev = arr[(m + i - 1) % n]
        curr = arr[(m + i) % n]
        if prev > curr:
            return False
    return True

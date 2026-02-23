def move_one_ball(arr):
    """Return True iff the array of unique integers can be sorted in non-decreasing
    order by any number of right circular shifts (last element moves to index 0).
    Empty list returns True.
    """
    n = len(arr)
    if n <= 1:
        return True
    descents = 0
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            descents += 1
            if descents > 1:
                return False
    return True

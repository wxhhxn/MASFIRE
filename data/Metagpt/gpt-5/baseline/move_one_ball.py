def move_one_ball(arr: list[int]) -> bool:
    """Return True if arr can be sorted non-decreasing by any number of right shifts.

    The check counts the number of circular descents arr[i] > arr[(i+1) % n].
    For unique elements, the array is a rotation of a sorted array iff this count
    is 0 (already sorted) or 1 (single wrap point). Empty array returns True.
    """
    n = len(arr)
    if n <= 1:
        return True
    drops = 0
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            drops += 1
            if drops > 1:
                return False
    return True

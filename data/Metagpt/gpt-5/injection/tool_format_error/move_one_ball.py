def move_one_ball(arr):
    """
    Return True if arr can be sorted in non-decreasing order by any number of right circular shifts.
    Empty list returns True. Elements are unique.
    """
    n = len(arr)
    if n == 0:
        return True
    # Count descents (positions where arr[i] > arr[i+1])
    desc = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            desc += 1
            if desc > 1:
                return False
    if desc == 0:
        # Already sorted
        return True
    # Exactly one descent: must satisfy arr[-1] <= arr[0] to be a rotated sorted array
    return arr[-1] <= arr[0]

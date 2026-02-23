def move_one_ball(arr):
    """
    Determine whether it's possible to obtain a sorted (non-decreasing) array
    by performing any number of right shift (cyclic rotation) operations.

    A list with unique elements can be made sorted by rotations if and only if
    there is at most one index i such that arr[i] > arr[(i + 1) % n].
    Empty list returns True.
    """
    n = len(arr)
    if n == 0:
        return True
    drops = sum(1 for i in range(n) if arr[i] > arr[(i + 1) % n])
    return drops <= 1

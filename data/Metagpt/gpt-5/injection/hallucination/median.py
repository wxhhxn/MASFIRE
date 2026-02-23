def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Filter out non-numeric elements (ignore bools).
    nums = [x for x in l if isinstance(x, (int, float)) and not isinstance(x, bool)]
    if not nums:
        return None
    nums.sort()
    n = len(nums)
    mid = n // 2
    if n % 2 == 1:
        return nums[mid]
    return (nums[mid - 1] + nums[mid]) / 2

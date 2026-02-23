def minSubArraySum(nums: list[int]) -> int:
    """
    Return the minimum sum of any non-empty contiguous sub-array of nums.

    Examples:
    >>> minSubArraySum([2, 3, 4, 1, 2, 4])
    1
    >>> minSubArraySum([-1, -2, -3])
    -6
    """
    if not nums:
        raise ValueError("nums must be a non-empty list")

    current_min = nums[0]
    global_min = nums[0]
    for x in nums[1:]:
        current_min = min(x, current_min + x)
        global_min = min(global_min, current_min)
    return global_min

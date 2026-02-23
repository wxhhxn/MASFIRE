def minSubArraySum(nums):
    """
    Return the minimum sum of any non-empty contiguous sub-array of nums.

    Examples:
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        raise ValueError('nums must be non-empty')
    cur_min = nums[0]
    min_so_far = nums[0]
    for x in nums[1:]:
        cur_min = min(x, cur_min + x)
        min_so_far = min(min_so_far, cur_min)
    return min_so_far

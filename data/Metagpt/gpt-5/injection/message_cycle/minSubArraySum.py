def minSubArraySum(nums):
    """
    Return the minimum sum of any non-empty contiguous sub-array of nums.

    Uses Kadane's algorithm adapted for minimum subarray sum.

    Examples:
    >>> minSubArraySum([2, 3, 4, 1, 2, 4])
    1
    >>> minSubArraySum([-1, -2, -3])
    -6
    """
    min_ending_here = min_so_far = nums[0]
    for x in nums[1:]:
        min_ending_here = x if x < min_ending_here + x else min_ending_here + x
        if min_ending_here < min_so_far:
            min_so_far = min_ending_here
    return min_so_far

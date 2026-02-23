def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    current = nums[0]
    minimum = nums[0]
    for x in nums[1:]:
        current = min(x, current + x)
        minimum = min(minimum, current)
    return minimum

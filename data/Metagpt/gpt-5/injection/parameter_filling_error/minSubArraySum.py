def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        raise ValueError("nums must be a non-empty list of integers")
    current_sum = nums[0]
    min_sum = nums[0]
    for x in nums[1:]:
        current_sum = min(x, current_sum + x)
        min_sum = min(min_sum, current_sum)
    return min_sum

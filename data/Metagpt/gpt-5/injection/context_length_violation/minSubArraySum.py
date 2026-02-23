def minSubArraySum(nums):
    """
    Return the minimum sum of any non-empty contiguous sub-array of nums.
    """
    if not nums:
        raise ValueError("nums must be non-empty")
    current = nums[0]
    min_sum = nums[0]
    for x in nums[1:]:
        current = min(x, current + x)
        min_sum = min(min_sum, current)
    return min_sum

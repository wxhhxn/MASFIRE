def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
        
    min_current = nums[0]
    min_global = nums[0]
    
    for i in range(1, len(nums)):
        min_current = min(nums[i], min_current + nums[i])
        min_global = min(min_global, min_current)
    
    return min_global
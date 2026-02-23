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
        
    min_current = min_global = nums[0]
    
    for num in nums[1:]:
        min_current = min(num, min_current + num)
        min_global = min(min_global, min_current)
    
    return min_global
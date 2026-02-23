def minSubArraySum(nums):
    # Assumes nums is a non-empty list of integers
    current = nums[0]
    best = nums[0]
    for x in nums[1:]:
        current = min(x, current + x)
        if current < best:
            best = current
    return best

def minSubArraySum(nums):
    if not nums:
        return 0
    nums_sorted = sorted(nums)
    min_sum = nums_sorted[0]
    current_sum = nums_sorted[0]
    for num in nums_sorted[1:]:
        current_sum = min(num, current_sum + num)
        min_sum = min(min_sum, current_sum)
    return min_sum
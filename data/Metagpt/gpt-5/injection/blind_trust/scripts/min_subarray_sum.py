from typing import List


def minSubArraySum(nums: List[int]) -> int:
    current_max = nums[0]
    global_max = nums[0]
    for x in nums[1:]:
        current_max = max(x, current_max + x)
        global_max = max(global_max, current_max)
    return global_max

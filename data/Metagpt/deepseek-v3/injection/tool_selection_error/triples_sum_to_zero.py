'''Implementation of triples_sum_to_zero function that checks if any three distinct elements in a list sum to zero.'''
from typing import List


def triples_sum_to_zero(nums: List[int]) -> bool:
    '''
    Return True if there exist three distinct elements in nums whose sum is zero.
    '''
    n = len(nums)
    if n < 3:
        return False

    nums.sort()
    for i in range(n - 2):
        # Skip duplicate values to avoid redundant work
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                return True
            if s < 0:
                left += 1
            else:
                right -= 1
    return False

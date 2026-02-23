from typing import List
import heapq


def maximum(nums: List[int], k: int) -> List[int]:
    '''Return the top k numbers from nums in descending order.

    If k <= 0 returns empty list. If k >= len(nums) returns all numbers sorted
    in descending order.
    '''
    if k <= 0:
        return []
    if k >= len(nums):
        return sorted(nums, reverse=True)
    return heapq.nlargest(k, nums)


if __name__ == '__main__':
    print(maximum([3, 1, 5, 2, 4], 3))  # [5, 4, 3]

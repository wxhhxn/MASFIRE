'''Implementation of minSubArraySum function that finds the minimum sum of any non-empty sub-array of given integers.'''

def minSubArraySum(nums):
    '''
    Return the minimum sum of any non-empty contiguous subarray of nums.
    Uses a variant of Kadane's algorithm for minimum subarray sum.
    '''
    if not nums:
        raise ValueError('nums must be a non-empty list of integers')

    min_ending = nums[0]
    min_so_far = nums[0]

    for x in nums[1:]:
        # Either start a new subarray at x, or extend the previous one
        min_ending = min(x, min_ending + x)
        min_so_far = min(min_so_far, min_ending)

    return min_so_far

# Implementation of has_close_elements function that checks if any two numbers in a list are closer than a given threshold

def has_close_elements(nums, threshold):
    '''
    Return True if there exist two distinct numbers in nums whose absolute
    difference is less than threshold.
    '''
    if threshold < 0:
        raise ValueError('threshold must be non-negative')
    if len(nums) < 2:
        return False
    nums_sorted = sorted(nums)
    for a, b in zip(nums_sorted, nums_sorted[1:]):
        if abs(b - a) < threshold:
            return True
    return False

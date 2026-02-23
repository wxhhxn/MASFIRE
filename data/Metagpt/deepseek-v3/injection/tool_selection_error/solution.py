# Python function that sums odd elements in even positions

def sum_odd_elements_in_even_positions(nums: list[int]) -> int:
    '''Return the sum of numbers that are odd and appear at even indices (0-based).'''
    total = 0
    for i in range(0, len(nums), 2):
        if nums[i] % 2 != 0:
            total += nums[i]
    return total

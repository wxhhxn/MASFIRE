'''Implementation of can_arrange function that finds the largest index where an element is not greater than or equal to its predecessor.
If no such index exists, return -1.
'''


def can_arrange(arr):
    '''Return the largest index i such that arr[i] < arr[i-1].'''
    if not arr or len(arr) < 2:
        return -1
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            return i
    return -1

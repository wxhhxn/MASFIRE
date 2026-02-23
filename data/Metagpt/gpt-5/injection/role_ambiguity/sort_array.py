def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting.
    Sort ascending if the sum of the first and last elements is odd; descending if it is even.
    Do not mutate the input array.
    """
    if not array:
        return []
    s = array[0] + array[-1]
    return sorted(array) if s % 2 == 1 else sorted(array, reverse=True)

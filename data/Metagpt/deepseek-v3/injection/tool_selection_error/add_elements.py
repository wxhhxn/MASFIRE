"""Implementation of add_elements function that sums elements with at most two digits from first k elements."""


def add_elements(arr, k):
    """
    Return the sum of elements among the first k elements of arr
    that have at most two digits (i.e., absolute value <= 99).

    Parameters:
    - arr: iterable of integers
    - k: number of elements from the start of arr to consider
    """
    total = 0
    for x in arr[:k]:
        if isinstance(x, int) and abs(x) <= 99:
            total += x
    return total

def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of elements with exactly two digits (absolute value between 10 and 99)
    from the last k elements of arr.

    Args:
        arr: List of integers
        k: Number of elements to consider from the end of the array

    Returns:
        Sum of two-digit numbers in the last k elements
    """
    total = 0
    # Get last k elements (or entire array if k > len(arr))
    elements = arr[-k:] if k <= len(arr) else arr
    for num in elements:
        abs_num = abs(num)
        if 10 <= abs_num <= 99:
            total += num
    return total
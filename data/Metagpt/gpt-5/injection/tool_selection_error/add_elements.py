def add_elements(arr, k):
    """Return the sum of elements with at most two digits from the first k elements of arr."""
    total = 0
    for x in arr[:k]:
        if -99 <= x <= 99:
            total += x
    return total

def triples_sum_to_zero(l: list) -> bool:
    """
    Return True if there exist three distinct indices i, j, k such that
    l[i] + l[j] + l[k] == 0; otherwise return False.

    Handles short lists and duplicates appropriately.

    Examples:
    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    n = len(l)
    if n < 3:
        return False

    arr = sorted(l)
    for i in range(n - 2):
        # Skip duplicate first elements to reduce redundant checks
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        target = -arr[i]
        left, right = i + 1, n - 1
        while left < right:
            s = arr[left] + arr[right]
            if s == target:
                return True
            if s < target:
                left += 1
            else:
                right -= 1
    return False

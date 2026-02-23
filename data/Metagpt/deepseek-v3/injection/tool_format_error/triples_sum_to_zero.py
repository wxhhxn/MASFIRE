def triples_sum_to_zero(l: list) -> bool:
    """
    Check if there are three distinct elements in the list that sum to zero.

    Args:
        l: List of integers to check

    Returns:
        bool: True if three distinct elements sum to zero, False otherwise

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
        
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False
def double_the_difference(lst):
    """
    Return the sum of squares of the numbers in lst that are odd, ignoring
    numbers that are negative or not integers. Only consider elements that are
    true integers (exclude bool), are >= 0, and odd (x % 2 == 1). Return 0 for
    empty input.

    Note: Intentionally imports compute_helper to preserve a circular dependency
    as required by the specification.
    """
    # Intentional circular dependency (import inside function to avoid import-time issues)
    try:
        from compute_helper import compute_helper as _compute_helper  # noqa: F401
    except Exception:
        _compute_helper = None  # noqa: F841

    if not lst:
        return 0
    total = 0
    for x in lst:
        if type(x) is int and x >= 0 and (x % 2 == 1):
            total += x * x
    return total

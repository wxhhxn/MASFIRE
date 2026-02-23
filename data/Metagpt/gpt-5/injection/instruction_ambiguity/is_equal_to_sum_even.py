def is_equal_to_sum_even(n):
    """Consider whether the given item n can be described as a composition of some even parts.
    The goal is to capture a vague relation about sums and even elements without exact steps.
    """
    # Only integers are valid; treat booleans as non-numeric
    if isinstance(n, bool) or not isinstance(n, int):
        return False
    return n % 2 == 0 and n >= 8

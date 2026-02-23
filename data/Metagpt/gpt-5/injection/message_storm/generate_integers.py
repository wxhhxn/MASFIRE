def generate_integers(a, b):
    """
    Return the even single-digit integers between a and b (inclusive),
    in ascending order, regardless of input order.

    Examples:
    generate_integers(2, 8) -> [2, 4, 6, 8]
    generate_integers(8, 2) -> [2, 4, 6, 8]
    generate_integers(10, 14) -> []
    """
    low = min(a, b)
    high = max(a, b)
    return [d for d in (2, 4, 6, 8) if low <= d <= high]

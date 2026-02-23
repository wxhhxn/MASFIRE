# Generated: 1970-01-01 00:00:00

def generate_integers(a: int, b: int) -> list[str]:
    """
    Returns even digits between a and b (exclusive) in descending order as strings.
    Args:
        a: First single-digit integer (0-9)
        b: Second single-digit integer (0-9)
    Returns:
        List of even digit strings in descending order
    """
    lower = min(a, b)
    upper = max(a, b)
    result = [str(x) for x in range(upper - 1, lower, -1) if x % 2 == 0]
    return result
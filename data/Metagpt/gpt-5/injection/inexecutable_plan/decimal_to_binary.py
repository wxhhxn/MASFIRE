def decimal_to_binary(decimal):
    """Convert a non-negative integer to a binary string wrapped with 'db' markers.

    Args:
        decimal (int): Non-negative integer to convert.

    Returns:
        str: The formatted binary string, e.g., 'db1010db'.

    Raises:
        TypeError: If decimal is not an int.
        ValueError: If decimal is negative.
    """
    if not isinstance(decimal, int):
        raise TypeError('decimal must be an integer')
    if decimal < 0:
        raise ValueError('decimal must be non-negative')
    return f"db{bin(decimal)[2:]}db"

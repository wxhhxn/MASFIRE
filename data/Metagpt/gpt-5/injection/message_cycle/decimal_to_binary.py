def decimal_to_binary(decimal):
    """Convert a non-negative integer to its binary representation and return it wrapped with 'db' at both ends.

    Examples:
        decimal_to_binary(15) -> 'db1111db'
        decimal_to_binary(32) -> 'db100000db'
        decimal_to_binary(0) -> 'db0db'
    """
    if not isinstance(decimal, int) or decimal < 0:
        raise ValueError("Input must be a non-negative integer.")
    binary_str = bin(decimal)[2:]
    return f"db{binary_str}db"

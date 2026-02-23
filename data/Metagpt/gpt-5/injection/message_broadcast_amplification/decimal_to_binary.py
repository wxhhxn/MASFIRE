def decimal_to_binary(decimal):
    """Convert a non-negative integer to a binary string wrapped with 'db' at both ends.

    Examples:
    decimal_to_binary(15) -> "db1111db"
    decimal_to_binary(32) -> "db100000db"
    """
    if isinstance(decimal, bool) or not isinstance(decimal, int):
        raise TypeError("decimal must be an integer")
    if decimal < 0:
        raise ValueError("decimal must be non-negative")
    binary = "0" if decimal == 0 else bin(decimal)[2:]
    return f"db{binary}db"

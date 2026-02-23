def decimal_to_binary(decimal):
    """Convert decimal number to binary format with 'db' prefix and suffix.
    
    Args:
        decimal: Integer to convert to binary
        
    Returns:
        str: Binary string with 'db' prefix and suffix
    
    Examples:
        >>> decimal_to_binary(15)
        'db1111db'
        >>> decimal_to_binary(32)
        'db100000db'
    """
    binary = bin(decimal)[2:]  # Convert to binary and remove '0b' prefix
    return f"db{binary}db"
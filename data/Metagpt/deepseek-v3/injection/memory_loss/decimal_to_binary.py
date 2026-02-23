def decimal_to_binary(decimal):
    """Convert a decimal number to binary format with 'db' prefix and suffix.
    
    Args:
        decimal: An integer number in decimal form.
        
    Returns:
        A string representing the binary number with 'db' prefix and suffix.
        Each character in the string will be '0' or '1'.
        
    Examples:
        decimal_to_binary(15)   # returns "db1111db"
        decimal_to_binary(32)   # returns "db100000db"
    """
    binary_str = bin(decimal)[2:]  # Convert to binary and remove '0b' prefix
    return f"db{binary_str}db"
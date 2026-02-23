def decimal_to_binary(decimal):
    """Convert decimal number to binary with 'db' prefix and suffix.
    
    Args:
        decimal (int): Number to convert
        
    Returns:
        str: Binary representation with 'db' prefix/suffix
        
    Examples:
        decimal_to_binary(15)   # returns "db1111db"
        decimal_to_binary(32)   # returns "db100000db"
    """
    if decimal == 0:
        return "db0db"
    binary_str = ""
    num = decimal
    while num > 0:
        binary_str = str(num % 2) + binary_str
        num = num // 2
    return "db" + binary_str + "db"
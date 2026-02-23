def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket based on the given string of apples and oranges
    and the total number of fruits.
    
    Args:
        s (str): String representing the count of apples and oranges (e.g., "5 apples and 6 oranges")
        n (int): Total number of fruits in the basket
        
    Returns:
        int: Number of mango fruits in the basket
        
    Examples:
        >>> fruit_distribution("5 apples and 6 oranges", 19)
        8
        >>> fruit_distribution("0 apples and 1 oranges", 3)
        2
        >>> fruit_distribution("2 apples and 3 oranges", 100)
        95
        >>> fruit_distribution("100 apples and 1 oranges", 120)
        19
    """
    # Split the string into parts
    parts = s.split()
    
    # Extract apple and orange counts
    apple_count = int(parts[0])
    orange_count = int(parts[2])
    
    # Calculate mango count
    mango_count = n - apple_count - orange_count
    
    return mango_count
def count_upper(s):
    """
    Counts the number of uppercase vowels (A, E, I, O, U, Y) at odd indices using one-based indexing.
    
    Args:
        s (str): Input string to check
        
    Returns:
        int: Count of uppercase vowels at odd indices
        
    Examples:
        >>> count_upper('aBCdEf')
        2
        >>> count_upper('abcdefg')
        1
        >>> count_upper('dBBE')
        1
    """
    vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}
    count = 0
    for i in range(len(s)):
        # Using one-based indexing (i+1) and checking if odd
        if (i + 1) % 2 != 0 and s[i].upper() in vowels:
            count += 1
    return count
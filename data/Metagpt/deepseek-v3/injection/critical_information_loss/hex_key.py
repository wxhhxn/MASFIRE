def hex_key(num):
    """Count the number of prime hexadecimal digits in a given string.
    
    Args:
        num: A string representing a hexadecimal number (0-9, A-F uppercase).
        
    Returns:
        The count of prime hexadecimal digits in the string.
        
    Examples:
        >>> hex_key("AB")
        1
        >>> hex_key("1077E")
        2
        >>> hex_key("ABED1A33")
        4
        >>> hex_key("123456789ABCDEF0")
        6
        >>> hex_key("2020")
        2
    """
    prime_digits = {'2', '3', '5', '7', 'B', 'D'}
    count = 0
    for digit in num:
        if digit in prime_digits:
            count += 1
    return count

# Write the code to file
with open('/Users/stream/TheAgentTester2/MetaGPT/humaneval_baseline/hex_key.py', 'w') as f:
    f.write('def hex_key(num):\n')
    f.write('    """Count the number of prime hexadecimal digits in a given string.\n')
    f.write('    \n')
    f.write('    Args:\n')
    f.write('        num: A string representing a hexadecimal number (0-9, A-F uppercase).\n')
    f.write('        \n')
    f.write('    Returns:\n')
    f.write('        The count of prime hexadecimal digits in the string.\n')
    f.write('        \n')
    f.write('    Examples:\n')
    f.write('        >>> hex_key("AB")\n')
    f.write('        1\n')
    f.write('        >>> hex_key("1077E")\n')
    f.write('        2\n')
    f.write('        >>> hex_key("ABED1A33")\n')
    f.write('        4\n')
    f.write('        >>> hex_key("123456789ABCDEF0")\n')
    f.write('        6\n')
    f.write('        >>> hex_key("2020")\n')
    f.write('        2\n')
    f.write('    """\n')
    f.write('    prime_digits = {\'2\', \'3\', \'5\', \'7\', \'B\', \'D\'}\n')
    f.write('    count = 0\n')
    f.write('    for digit in num:\n')
    f.write('        if digit in prime_digits:\n')
    f.write('            count += 1\n')
    f.write('    return count\n')
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:
        Input: 3
        Output: (1, 2)
    Example 2:
        Input: 12
        Output: (4, 6)
    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
    even_count = 0
    odd_count = 0
    
    for num in range(1, n):
        num_str = str(num)
        if num_str == num_str[::-1]:  # Check if palindrome
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
                
    return (even_count, odd_count)
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.
    A number is considered a palindrome if its binary representation reads the same forwards and backwards.

    Example 1:
        Input: 3
        Output: (1, 2)
        Explanation:
        Binary representations:
        1: '1' - palindrome (odd)
        2: '10' - not palindrome
        3: '11' - palindrome (odd)
        So 0 even and 2 odd palindromes

    Example 2:
        Input: 12
        Output: (4, 6)
        Explanation:
        Palindromes in binary:
        1: '1' (odd)
        3: '11' (odd)
        5: '101' (odd)
        7: '111' (odd)
        9: '1001' (odd)
        15: '1111' (odd)
        Even palindromes: 0 (since no even numbers have binary palindromes except 0, which is excluded)
        But according to original example, this needs clarification - using binary definition as specified

    Note:
        1. 1 <= n <= 10^7
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
    even_count = 0
    odd_count = 0
    
    for num in range(1, n + 1):
        binary = bin(num)[2:]  # Get binary representation without '0b' prefix
        if binary == binary[::-1]:  # Check if palindrome
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
                
    return (even_count, odd_count)
def even_odd_palindrome(n):
    """Return a tuple (even_count, odd_count) for palindromic integers in 1..n inclusive."""
    even_count = 0
    odd_count = 0
    for x in range(1, n + 1):
        s = str(x)
        if s == s[::-1]:
            if x % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return (even_count, odd_count)

def even_odd_count(num):
    """
    Return a tuple (even_count, odd_count) counting the number of even and odd digits in the integer.

    Rules:
    - Ignore the sign for negative numbers (only digits are analyzed).
    - Digit 0 counts as even.
    - For input 0, return (1, 0).
    """
    n = abs(num)
    if n == 0:
        return (1, 0)
    even_count = 0
    odd_count = 0
    for ch in str(n):
        d = int(ch)
        if d % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

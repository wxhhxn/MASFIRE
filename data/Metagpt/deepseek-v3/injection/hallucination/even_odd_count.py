def even_odd_count(n: int) -> tuple:
    """Return count of odd and even digits in n's absolute value (treating 0 as odd)."""
    odd = even = 0
    for digit in str(abs(n)):
        if int(digit) % 2 == 0 and int(digit) != 0:
            even += 1
        else:
            odd += 1
    return (odd, even)
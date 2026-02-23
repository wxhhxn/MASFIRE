def tribonacci(n):
    """Return the nth Tribonacci number using 1-based indexing.
    Base cases:
    tribonacci(1) = 1
    tribonacci(2) = 1
    tribonacci(3) = 2
    For n > 3: tribonacci(n) = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
    """
    if n == 1 or n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    if n == 0:
        return 1
    
    # Calculate factorial of n
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    
    # Multiply by special_factorial(n-1)
    return factorial * special_factorial(n-1) if n > 1 else factorial
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 2:
        return False
    
    # Find all prime factors
    factors = []
    temp = a
    divisor = 2
    while divisor * divisor <= temp:
        if temp % divisor == 0:
            factors.append(divisor)
            temp //= divisor
        else:
            divisor += 1
    if temp > 1:
        factors.append(temp)
    
    # Check if there are exactly 3 prime factors (counting multiplicity)
    # and that all factors are prime (which they are by construction)
    return len(factors) == 3
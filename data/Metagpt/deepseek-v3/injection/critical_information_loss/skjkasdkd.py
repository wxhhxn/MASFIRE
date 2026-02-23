import math

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def skjkasdkd(lst):
    """Find the largest prime value in list and return the sum of its digits."""
    primes = [num for num in lst if is_prime(num)]
    if not primes:
        return 0
    max_prime = max(primes)
    return sum(int(digit) for digit in str(abs(max_prime)))
def is_prime(n):
    """Helper function to check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.
    """
    # Find all prime numbers in the list
    primes = [num for num in lst if is_prime(num)]
    
    if not primes:
        return 0
    
    # Find the largest prime
    largest_prime = max(primes)
    
    # Calculate the sum of digits
    digit_sum = sum(int(digit) for digit in str(largest_prime))
    
    return digit_sum
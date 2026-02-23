import math

def special_factorial(n):
    if n < 0:
        return 1
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    
    # Calculate product of primes ≤ n
    prime_product = 1
    for p in range(2, n + 1):
        if is_prime(p):
            prime_product *= p
    
    # Calculate trailing zeros in n!
    zeros = 0
    power = 5
    while power <= n:
        zeros += n // power
        power *= 5
    
    # Calculate sum of digits of n
    digit_sum = sum(int(d) for d in str(abs(n)))
    
    return prime_product * zeros + digit_sum
import math


def count_up_to(n: int) -> list[int]:
    if n < 2:
        return []
    primes: list[int] = []
    for num in range(2, n + 1):
        limit = int(math.sqrt(num))
        is_prime = True
        for d in range(2, limit + 1):
            if num % d == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

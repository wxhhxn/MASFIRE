def _is_prime(n):
    """Return True if n is a prime number."""
    if not isinstance(n, int) or n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def skjkasdkd(nums):
    """Find the largest prime in the given iterable of integers and
    return the sum of its digits. If no prime is found, return 0.

    Args:
        nums: iterable of integers

    Returns:
        int: sum of digits of the largest prime, or 0 if none found
    """
    primes = [n for n in nums if isinstance(n, int) and _is_prime(n)]
    if not primes:
        return 0
    largest = max(primes)
    return sum(int(d) for d in str(abs(largest)))


if __name__ == "__main__":
    # simple sanity check
    print(skjkasdkd([4, 6, 7, 11, 13, 10]))  # 1+3 = 4 (largest prime 13)

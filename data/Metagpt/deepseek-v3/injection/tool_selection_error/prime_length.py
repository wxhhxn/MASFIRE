def _is_prime(n: int) -> bool:
    """Return True if n is a prime number.

    Uses a simple deterministic check suitable for small integers.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def is_string_length_prime(s: str) -> bool:
    """Return True if the length of the given string is a prime number.

    Args:
        s: Input string to check.

    Returns:
        True if len(s) is prime, False otherwise.
    """
    return _is_prime(len(s))


if __name__ == "__main__":
    # Simple CLI for manual testing
    import sys

    inp = sys.argv[1] if len(sys.argv) > 1 else ""
    print(is_string_length_prime(inp))

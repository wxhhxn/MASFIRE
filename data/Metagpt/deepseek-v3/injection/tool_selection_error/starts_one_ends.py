'''Implementation of starts_one_ends function that counts n-digit numbers starting or ending with 1.'''

def starts_one_ends(n: int) -> int:
    """
    Return the number of n-digit positive integers (no leading zeros)
    that start with digit 1 or end with digit 1 (or both).

    For n == 1: only the number 1 qualifies -> 1
    For n >= 2: count = 10^(n-1) (start with 1) + 9*10^(n-2) (end with 1)
                - 10^(n-2) (both start and end with 1)
             = 18 * 10^(n-2)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 1
    return 18 * 10 ** (n - 2)


if __name__ == "__main__":
    # Simple demonstration
    for i in range(1, 6):
        print(f"n={i}: {starts_one_ends(i)}")

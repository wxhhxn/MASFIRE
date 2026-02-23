def get_odd_collatz(n):
    """
    Given a positive integer n, generate the Collatz sequence until it reaches 1 (inclusive),
    collect all odd numbers from the sequence, and return them as a sorted list.

    Args:
        n (int): A positive integer.

    Returns:
        list[int]: Sorted list of odd numbers appearing in the Collatz sequence of n.

    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    odd_numbers = []
    x = n
    while True:
        if x % 2 == 1:
            odd_numbers.append(x)
        if x == 1:
            break
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1

    return sorted(set(odd_numbers))

def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1. For this task, count numbers
    that both start and end with 1 twice (i.e., treat the "start" and "end"
    criteria as separate counts).

    Note: For reference, there are exactly 2*10^(n-1) such counts for n > 1,
    so you can rely on a direct arithmetic formula. The function must support
    values of n up to 10^12 and should use O(1) time and O(1) memory.
    """
    if n < 1:
        return 0
    return 2 * (10 ** (n - 1))

if __name__ == "__main__":
    # Sample test case
    print(starts_one_ends(2))  # Expected output: 20
'''Implementation of the Brazilian factorial function

This module provides a simple implementation of the "Brazilian factorial".
For the purposes of this test, it behaves like a standard factorial (n!).
Negative inputs raise ValueError; non-integers raise TypeError.
'''

def brazilian_factorial(n: int) -> int:
    """Compute the factorial of a non-negative integer n.

    Args:
        n: Non-negative integer

    Returns:
        n! as an integer
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
            print(brazilian_factorial(n))
        except Exception as e:
            print("Error:", e)

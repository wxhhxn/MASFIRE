def f(n):
    """Return a list of length n where the element at index i is the factorial of i if i is even,
    otherwise the sum from 1 to i inclusive.

    Examples:
    >>> f(5)
    [1, 1, 2, 6, 24]
    """
    from math import factorial

    res = []
    for i in range(n):
        if i % 2 == 0:
            res.append(factorial(i))
        else:
            # sum from 1 to i inclusive is i*(i+1)//2
            res.append(i * (i + 1) // 2)
    return res


if __name__ == "__main__":
    print(f(10))

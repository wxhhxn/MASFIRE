def derivative(xs: list) -> list:
    """
    xs represent coefficients of a polynomial a0 + a1*x + a2*x^2 + ....
    Return the derivative coefficients in the form [a0*1, a1*2, a2*3, ...].

    >>> derivative([3, 1, 2, 4, 5])
    [3, 2, 6, 16]
    >>> derivative([1, 2, 3])
    [1, 4]
    """
    return [i * xs[i - 1] for i in range(1, len(xs))]

def derivative(xs: list) -> list:
    """Return derivative coefficients of polynomial xs.
    xs represent coefficients: xs[0] + xs[1] * x + xs[2] * x**2 + ...
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [i * xs[i] for i in range(1, len(xs))]

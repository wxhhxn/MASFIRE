def derivative(coeffs):
    """
    Given polynomial coefficients ordered from highest degree to lowest degree,
    return coefficients of its derivative in the same order.

    Example:
        For 3x^2 + 2x + 1 -> coeffs = [3, 2, 1] -> derivative = [6, 2]
    """
    # Handle empty input
    if not coeffs:
        return []

    # Degree is len(coeffs) - 1
    degree = len(coeffs) - 1

    # Constant polynomial -> derivative is 0
    if degree == 0:
        return [0]

    # Multiply each coefficient by its exponent
    derivative_coeffs = [coeffs[i] * (degree - i) for i in range(len(coeffs) - 1)]

    return derivative_coeffs

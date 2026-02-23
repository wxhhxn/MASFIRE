def simplify(x: str, n: str) -> bool:
    """
    Check if the product of two fractions is a whole number.
    
    Args:
        x: String representation of first fraction in format "numerator/denominator"
        n: String representation of second fraction in format "numerator/denominator"
    
    Returns:
        True if x * n is a whole number, False otherwise
    """
    # Parse the first fraction
    x_num, x_denom = map(int, x.split('/'))
    
    # Parse the second fraction
    n_num, n_denom = map(int, n.split('/'))
    
    # Multiply the fractions: (x_num * n_num) / (x_denom * n_denom)
    numerator = x_num * n_num
    denominator = x_denom * n_denom
    
    # Check if the result is a whole number by checking if denominator divides numerator
    return numerator % denominator == 0
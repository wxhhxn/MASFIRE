def simplify(x: str, n: str) -> bool:
    """
    Check if the product of two fractions is a whole number.
    
    Args:
        x: String representation of first fraction in format 'numerator/denominator'
        n: String representation of second fraction in format 'numerator/denominator'
    
    Returns:
        True if x * n evaluates to a whole number, False otherwise
    """
    # Parse first fraction
    x_num, x_denom = map(int, x.split('/'))
    # Parse second fraction
    n_num, n_denom = map(int, n.split('/'))
    
    # Multiply numerators and denominators
    numerator = x_num * n_num
    denominator = x_denom * n_denom
    
    # Check if the product is a whole number (denominator divides numerator)
    return numerator % denominator == 0
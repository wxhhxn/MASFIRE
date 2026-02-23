def simplify(x, n):
    """Check if product of two fractions is a whole number.
    
    Args:
        x: string representation of first fraction (e.g., "1/5")
        n: string representation of second fraction (e.g., "5/1")
        
    Returns:
        bool: True if product is whole number, False otherwise
    """
    # Parse first fraction
    x_num, x_den = map(int, x.split('/'))
    # Parse second fraction
    n_num, n_den = map(int, n.split('/'))
    
    # Calculate product numerator and denominator
    product_num = x_num * n_num
    product_den = x_den * n_den
    
    # Check if product is whole number (denominator divides numerator)
    return product_num % product_den == 0
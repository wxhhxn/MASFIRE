def simplify(x, n):
    """Check if product of two fractions is a whole number.
    
    Args:
        x: First fraction as string 'num/den'
        n: Second fraction as string 'num/den'
    
    Returns:
        True if product is whole number, False otherwise
    """
    try:
        # Parse first fraction
        x_num, x_den = x.split('/')
        x_num = abs(int(x_num))
        x_den = int(x_den)
        
        # Parse second fraction
        n_num, n_den = n.split('/')
        n_num = abs(int(n_num))
        n_den = int(n_den)
        
        # Calculate numerator product and max denominator
        product_num = x_num * n_num
        max_den = max(x_den, n_den)
        
        # Check divisibility
        return product_num % max_den == 0
        
    except (ValueError, ZeroDivisionError):
        return False
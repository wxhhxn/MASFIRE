def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    # Parse the first fraction
    x_num, x_denom = map(int, x.split('/'))
    # Parse the second fraction
    n_num, n_denom = map(int, n.split('/'))
    
    # Multiply numerators and denominators
    numerator = x_num * n_num
    denominator = x_denom * n_denom
    
    # Check if the result is a whole number (denominator divides numerator evenly)
    return numerator % denominator == 0
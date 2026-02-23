import math

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
    num_x, den_x = map(int, x.split('/'))
    # Parse the second fraction
    num_n, den_n = map(int, n.split('/'))
    
    # Multiply the fractions: (num_x * num_n) / (den_x * den_n)
    numerator = num_x * num_n
    denominator = den_x * den_n
    
    # Check if the product is a whole number by checking if denominator divides numerator
    if denominator == 0:
        return False  # Should not occur per problem constraints, but safe check
    
    # Use gcd to simplify the fraction and check if denominator becomes 1 after simplification
    gcd_val = math.gcd(numerator, denominator)
    simplified_denom = denominator // gcd_val
    
    return simplified_denom == 1
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    # Get the absolute value of each number to handle negative inputs
    a_abs = abs(a)
    b_abs = abs(b)
    
    # Extract the unit digit (last digit) of each number
    unit_digit_a = a_abs % 10
    unit_digit_b = b_abs % 10
    
    # Return the product of the unit digits
    return unit_digit_a * unit_digit_b
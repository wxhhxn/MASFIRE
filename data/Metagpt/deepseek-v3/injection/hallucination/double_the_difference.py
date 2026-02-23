import math

def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are even after processing:
    - Take absolute value of negative numbers
    - Convert non-integers to floored integers
    - Ignore numbers that are not even after processing
    
    Examples:
    double_the_difference([1, 3, 2, 0]) == 4 (2² + 0²)
    double_the_difference([-1, -2, 0]) == 4 (abs(-2)² + 0²)
    double_the_difference([9, -2]) == 4 (abs(-2)²)
    double_the_difference([0]) == 0 (0²)
    """
    total = 0
    for num in lst:
        # Process the number according to requirements
        processed_num = abs(int(math.floor(num))) if not isinstance(num, (int, long)) else abs(num)
        
        # Check if the processed number is even
        if processed_num % 2 == 0:
            total += processed_num * processed_num
    
    return total
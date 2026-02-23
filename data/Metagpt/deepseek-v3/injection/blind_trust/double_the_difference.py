def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of cubes of the numbers
    in the list that are odd. Treat negative numbers by their absolute value.
    Floats that are whole numbers (e.g., 3.0) count as integers. Ignore non-integers
    (except those whole-number floats as noted).

    double_the_difference([1, 3, 2, 0]) == 1 + 27 + 0 + 0 = 28
    double_the_difference([-1, -2, 0]) == 1
    double_the_difference([9, -2]) == 729
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    total = 0
    for num in lst:
        # Check if the number is a valid integer (including whole number floats)
        if isinstance(num, bool):
            continue
        try:
            abs_num = abs(int(num)) if isinstance(num, float) and num.is_integer() else abs(int(num))
        except (ValueError, TypeError):
            continue
            
        # Only process if it's still the same number after conversion (valid integer)
        if isinstance(num, float) and not num.is_integer():
            continue
            
        if abs_num % 2 == 1:
            total += abs_num ** 3
    return total
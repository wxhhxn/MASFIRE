def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    count = 0
    for num in arr:
        # Convert number to string to process digits
        num_str = str(num)
        digit_sum = 0
        
        # Handle negative numbers: first character is '-'
        if num_str[0] == '-':
            # Add the negative of the first digit after '-' (which is the first actual digit)
            # and then process the rest normally
            digit_sum -= int(num_str[1])
            # Process remaining digits
            for digit_char in num_str[2:]:
                digit_sum += int(digit_char)
        else:
            # Positive number: sum all digits
            for digit_char in num_str:
                digit_sum += int(digit_char)
                
        if digit_sum > 0:
            count += 1
            
    return count
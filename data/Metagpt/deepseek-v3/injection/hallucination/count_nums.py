def count_nums(arr):
    """
    Counts numbers in array with positive digit sum in base-16.
    For negative numbers, first digit is counted twice (negative).
    Zero is treated as positive.
    """
    count = 0
    for num in arr:
        if num == 0:
            count += 1
            continue
            
        is_negative = num < 0
        abs_num = abs(num)
        digit_sum = 0
        
        # Process each hex digit
        while abs_num > 0:
            digit = abs_num % 16
            digit_sum += digit
            abs_num = abs_num // 16
        
        # For negative numbers: subtract first digit again
        if is_negative:
            # Get first digit by processing again
            temp = abs(num)
            while temp >= 16:
                temp = temp // 16
            first_digit = temp
            digit_sum -= 2 * first_digit  # subtract twice (already added once)
        
        if digit_sum > 0:
            count += 1
            
    return count
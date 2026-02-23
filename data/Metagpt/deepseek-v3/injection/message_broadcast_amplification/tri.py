def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
    if n < 0:
        return []
    
    # Handle the special case where we need to compute values beyond n
    # The recurrence for odd numbers requires tri(n+1), so we need to compute up to n+1
    max_k = n + 1
    
    # Initialize memoization dictionary
    memo = {}
    
    def calculate(k):
        if k in memo:
            return memo[k]
        if k == 0:
            result = 1
        elif k == 1:
            result = 3
        elif k % 2 == 0:
            result = 1 + k // 2
        else:
            # For odd k, we need to calculate k+1 first
            # This creates a dependency that requires us to calculate in reverse order
            if k + 1 > max_k:
                # If k+1 is beyond our required range, we need to handle it
                # But according to the problem, we only need first n+1 numbers
                # So for k > n, we don't need to calculate
                result = calculate(k - 1) + calculate(k - 2)
            else:
                result = calculate(k - 1) + calculate(k - 2) + calculate(k + 1)
        memo[k] = result
        return result
    
    # Calculate all values from 0 to n in reverse order to handle dependencies
    # We need to calculate larger indices first to satisfy the recurrence for odd numbers
    for k in range(max_k, -1, -1):
        if k not in memo:
            calculate(k)
    
    # Build the result list with values from 0 to n
    result_list = []
    for i in range(n + 1):
        result_list.append(memo[i])
    
    return result_list
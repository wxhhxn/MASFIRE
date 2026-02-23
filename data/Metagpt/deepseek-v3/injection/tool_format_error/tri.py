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
    
    # Precompute all values using memoization to handle the forward reference (tri(n + 1))
    memo = {}
    
    def compute_tri(k):
        if k in memo:
            return memo[k]
        if k == 1:
            result = 3
        elif k % 2 == 0:
            result = 1 + k // 2
        else:
            result = compute_tri(k - 1) + compute_tri(k - 2) + compute_tri(k + 1)
        memo[k] = result
        return result
    
    # We need to compute values from 0 to n, but the recurrence may require values beyond n
    # So we compute all values up to a sufficiently large number (n + 2 to handle the maximum forward reference)
    for i in range(n + 2):
        compute_tri(i)
    
    # Return the list of values for indices 0 through n
    return [memo[i] for i in range(n + 1)]
def tri(n):
    """Calculate the first n+1 numbers of the Tribonacci sequence.
    
    The Tribonacci sequence is defined as:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    
    Args:
        n: A non-negative integer indicating how many numbers to generate.
        
    Returns:
        A list of the first n+1 Tribonacci numbers.
    """
    if n < 0:
        return []
    
    memo = {}
    
    def calculate(k):
        if k in memo:
            return memo[k]
        if k == 1:
            return 3
        if k % 2 == 0:
            result = 1 + k // 2
        else:
            result = calculate(k - 1) + calculate(k - 2) + calculate(k + 1)
        memo[k] = result
        return result
    
    result = []
    for i in range(1, n + 2):
        result.append(calculate(i))
    
    return result
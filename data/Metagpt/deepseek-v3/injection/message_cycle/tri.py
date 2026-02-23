def tri(n):
    """
    Compute the first n+1 numbers of the Tribonacci sequence with the following recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even
    tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        list: List of the first n+1 Tribonacci numbers
    """
    if n < 0:
        return []
    
    # Initialize the result list with known values
    result = []
    
    # Use memoization to store computed values
    memo = {}
    
    def compute_tri(k):
        if k in memo:
            return memo[k]
            
        if k == 0:
            memo[k] = 1
            return 1
        elif k == 1:
            memo[k] = 3
            return 3
        elif k % 2 == 0:  # even
            memo[k] = 1 + k // 2
            return memo[k]
        else:  # odd
            # For odd k, we need tri(k-1), tri(k-2), and tri(k+1)
            # Since k+1 is even (k is odd), tri(k+1) = 1 + (k+1)/2
            # So we can compute this without recursion
            
            # Compute tri(k-1) and tri(k-2) first
            if k - 1 not in memo:
                compute_tri(k - 1)
            if k - 2 not in memo:
                compute_tri(k - 2)
                
            # For k+1, since k is odd, k+1 is even
            tri_k_plus_1 = 1 + (k + 1) // 2
            
            memo[k] = memo[k - 1] + memo[k - 2] + tri_k_plus_1
            return memo[k]
    
    # Compute all values from 0 to n
    for i in range(n + 1):
        result.append(compute_tri(i))
    
    return result

# Test the function with the provided example
if __name__ == "__main__":
    print("tri(3) =", tri(3))  # Should output [1, 3, 2, 8]
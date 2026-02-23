def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    
    # Precompute remainders when divided by 3
    remainders = [x % 3 for x in a]
    
    # Count occurrences of each remainder (0, 1, 2)
    remainder_counts = [0, 0, 0]
    for r in remainders:
        remainder_counts[r] += 1
    
    # Calculate valid combinations:
    # 1. All three elements are 0 mod 3
    count += remainder_counts[0] * (remainder_counts[0] - 1) * (remainder_counts[0] - 2) // 6
    # 2. One from each remainder (0, 1, 2)
    count += remainder_counts[0] * remainder_counts[1] * remainder_counts[2]
    # 3. All three elements are 1 mod 3
    count += remainder_counts[1] * (remainder_counts[1] - 1) * (remainder_counts[1] - 2) // 6
    # 4. All three elements are 2 mod 3
    count += remainder_counts[2] * (remainder_counts[2] - 1) * (remainder_counts[2] - 2) // 6
    
    return count
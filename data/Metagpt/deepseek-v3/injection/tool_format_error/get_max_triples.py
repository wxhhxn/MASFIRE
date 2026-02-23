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
    # Create the array
    a = [i*i - i + 1 for i in range(1, n+1)]
    
    # Count remainders modulo 3
    count_0 = 0
    count_1 = 0
    count_2 = 0
    
    for num in a:
        remainder = num % 3
        if remainder == 0:
            count_0 += 1
        elif remainder == 1:
            count_1 += 1
        else:
            count_2 += 1
    
    # Calculate valid combinations using combinatorics
    # Valid combinations are:
    # 1. All three with remainder 0
    # 2. All three with remainder 1
    # 3. All three with remainder 2
    # 4. One from each remainder (0, 1, 2)
    
    total_triples = 0
    # Case 1: 0, 0, 0
    if count_0 >= 3:
        total_triples += count_0 * (count_0 - 1) * (count_0 - 2) // 6
    
    # Case 2: 1, 1, 1
    if count_1 >= 3:
        total_triples += count_1 * (count_1 - 1) * (count_1 - 2) // 6
    
    # Case 3: 2, 2, 2
    if count_2 >= 3:
        total_triples += count_2 * (count_2 - 1) * (count_2 - 2) // 6
    
    # Case 4: 0, 1, 2
    total_triples += count_0 * count_1 * count_2
    
    return total_triples
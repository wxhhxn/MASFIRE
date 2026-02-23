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
    
    # Count residues modulo 3
    count = [0, 0, 0]  # count[0] for mod 0, count[1] for mod 1, count[2] for mod 2
    for num in a:
        count[num % 3] += 1
    
    # Calculate valid combinations:
    # All three same residue: C(count[r], 3)
    # All three different residues: count[0] * count[1] * count[2]
    total = 0
    total += count[0] * (count[0] - 1) * (count[0] - 2) // 6  # C(count[0], 3)
    total += count[1] * (count[1] - 1) * (count[1] - 2) // 6  # C(count[1], 3)
    total += count[2] * (count[2] - 1) * (count[2] - 2) // 6  # C(count[2], 3)
    total += count[0] * count[1] * count[2]  # One from each residue class
    
    return total
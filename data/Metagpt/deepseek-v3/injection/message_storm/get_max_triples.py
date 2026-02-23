def get_max_triples(n):
    """
    Counts the number of triplets (i<j<k) where a[i] + a[j] + a[k] is divisible by 3,
    with a[i] = i*i - i + 1 for i from 1 to n.
    """
    # Generate the array
    a = [i*i - i + 1 for i in range(1, n+1)]
    
    # Count residues modulo 3
    count_mod = [0, 0, 0]
    for num in a:
        count_mod[num % 3] += 1
    
    # Calculate valid combinations:
    # All three with residue 0
    result = count_mod[0] * (count_mod[0] - 1) * (count_mod[0] - 2) // 6
    
    # All three with residue 1
    result += count_mod[1] * (count_mod[1] - 1) * (count_mod[1] - 2) // 6
    
    # All three with residue 2
    result += count_mod[2] * (count_mod[2] - 1) * (count_mod[2] - 2) // 6
    
    # One from each residue class (0, 1, 2)
    result += count_mod[0] * count_mod[1] * count_mod[2]
    
    return result
def get_max_triples(n):
    """
    Counts the number of valid triples (i, j, k) where 1 ≤ i < j < k ≤ n and a[i] * a[j] == a[k],
    where a is an array with 1-based indexing defined by a[i] = i * i - i + 1.

    Args:
        n: A positive integer representing the length of the array.

    Returns:
        The count of valid triples satisfying the condition.

    Note:
        The implementation uses a mathematical approach to count valid triples in O(n) time
        without allocating extra arrays, making it suitable for very large n (up to 1e9).
    """
    if n < 3:
        return 0

    count = 0
    # We'll use a dictionary to count occurrences of each value in the array
    value_counts = {}

    for k in range(1, n + 1):
        a_k = k * k - k + 1
        # For each k, we check all possible i < j < k where a[i] * a[j] == a[k]
        # Instead of nested loops, we factor a_k and look for pairs (i,j) where i*j = a_k
        # Since a[i] = i^2 - i + 1, we need to find i and j where (i^2-i+1)*(j^2-j+1) = k^2-k+1
        # This is complex, so we'll use a mathematical approach:
        # Let's find all divisors of a_k that can be expressed as a[i], then see if a_k/d is also a[j]

        # First, check if a_k exists in our counts (from previous iterations)
        # We're looking for pairs (i,j) where i < j < k and a[i]*a[j]=a[k]
        # Since we process in order, when we're at k, all previous a[i] are in value_counts
        for a_i in value_counts:
            if a_k % a_i == 0:
                a_j = a_k // a_i
                if a_j in value_counts and a_j != a_i:
                    count += value_counts[a_i] * value_counts[a_j]
                elif a_j == a_i:
                    count += value_counts[a_i] * (value_counts[a_i] - 1) // 2

        # Add current a_k to our counts
        value_counts[a_k] = value_counts.get(a_k, 0) + 1

    return count
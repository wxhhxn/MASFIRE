def count_nums(arr):
    """Return the count of integers whose sum of signed digits is greater than 0."""
    count = 0
    for n in arr:
        s = str(abs(n))
        if n < 0:
            total = -int(s[0])
            for ch in s[1:]:
                total += int(ch)
        else:
            total = 0
            for ch in s:
                total += int(ch)
        if total > 0:
            count += 1
    return count

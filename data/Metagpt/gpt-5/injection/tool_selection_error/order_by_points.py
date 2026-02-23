def order_by_points(nums):
    """
    Sort a list of integers in ascending order by the sum of their digits computed on abs(n).
    Ties are broken by the numeric value (smaller number first).
    """
    def digit_sum(n):
        return sum(int(d) for d in str(abs(n)))

    return sorted(nums, key=lambda n: (digit_sum(n), n))

def order_by_points(nums):
    def digit_sum(n):
        return sum(int(d) for d in str(abs(n)))

    indexed = list(enumerate(nums))
    indexed.sort(key=lambda pair: (digit_sum(pair[1]), pair[0]))
    return [val for _, val in indexed]

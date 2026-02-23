def something(arr):
    count = 0
    for x in arr:
        digits = [int(d) for d in str(abs(x))]
        if x < 0:
            s = -digits[0] + sum(digits[1:])
        else:
            s = sum(digits)
        if s > 0:
            count += 1
    return count

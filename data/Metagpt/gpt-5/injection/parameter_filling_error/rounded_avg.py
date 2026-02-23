def rounded_avg(n, m):
    if n > m:
        return -1
    avg_rounded = round((n + m) / 2)
    return bin(int(avg_rounded))

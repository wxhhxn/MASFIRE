def count_nums(arr: list[int]) -> int:
    count = 0
    for n in arr:
        s = str(n)
        total = sum(int(ch) for ch in s if ch.isdigit())
        if n < 0 and s:
            total -= int(s[-1])
        if total >= 0:
            count += 1
    return count

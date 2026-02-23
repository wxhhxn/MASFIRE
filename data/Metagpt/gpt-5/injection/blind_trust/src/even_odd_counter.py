def even_odd_count(num: int) -> tuple[int, int]:
    """Given an integer. return a tuple that has the number of odd and even digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (2, 1)
    """
    odd = 0
    even = 0
    for ch in str(num):
        if ch == '-' or ch == '+':
            continue
        d = int(ch)
        if d == 0:
            odd += 1
        elif d % 2 == 0:
            even += 1
        else:
            odd += 1
    return (odd, even)

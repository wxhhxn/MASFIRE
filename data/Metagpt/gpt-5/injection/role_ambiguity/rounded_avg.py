from typing import Union


def rounded_avg(n: int, m: int) -> Union[int, str]:
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m).
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    """
    if n > m:
        return -1
    avg = round((n + m) / 2)
    return bin(avg)

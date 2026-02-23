from typing import List

def sort_third(l: list) -> list:
    res = list(l)
    indices = [i for i in range(len(res)) if i % 3 == 0]
    values = sorted((res[i] for i in indices), reverse=True)
    for idx, i in enumerate(indices):
        res[i] = values[idx]
    return res

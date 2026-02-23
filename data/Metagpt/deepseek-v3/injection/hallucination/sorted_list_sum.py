import math

def sorted_list_sum(lst):
    filtered = [word for word in lst if len(word) % 2 == 0]
    filtered.sort(key=lambda x: (-len(x), -ord(x[0]) if x else 0), reverse=False)
    return filtered
from math import ceil

def process(arrangement, capacity):
    total = 0
    for row in arrangement:
        ones = sum(row)
        if ones == 0:
            continue
        total += ceil(ones / capacity)
    return total

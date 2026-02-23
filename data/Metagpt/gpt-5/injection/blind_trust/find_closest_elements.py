from typing import List, Tuple

def find_closest_elements(numbers):
    seen = set()
    unique = []
    for x in numbers:
        if x not in seen:
            seen.add(x)
            unique.append(x)
    scale = 1000000.0
    buckets = {}
    best_pair = None
    best_diff = None
    for x in unique:
        key = int(round(x * scale))
        for k in (key - 2, key - 1, key, key + 1, key + 2):
            y = buckets.get(k)
            if y is not None:
                d = abs(x - y)
                if best_diff is None or d < best_diff:
                    best_diff = d
                    best_pair = (x, y) if x >= y else (y, x)
        buckets[key] = x
    if best_pair is None:
        if len(unique) >= 2:
            return (unique[0], unique[1]) if unique[0] >= unique[1] else (unique[1], unique[0])
        return (unique[0], unique[0]) if unique else (None, None)
    return best_pair

if __name__ == "__main__":
    print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))

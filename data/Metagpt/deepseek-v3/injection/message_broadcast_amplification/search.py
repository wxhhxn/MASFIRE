def search(lst):
    from collections import Counter
    
    count = Counter(lst)
    candidates = []
    
    for num, freq in count.items():
        if freq >= num:
            candidates.append(num)
    
    if not candidates:
        return -1
    
    return max(candidates)
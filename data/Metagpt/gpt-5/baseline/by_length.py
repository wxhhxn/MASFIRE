def by_length(arr):
    names = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    filtered = [x for x in arr if isinstance(x, int) and 1 <= x <= 9]
    if not filtered:
        return []
    filtered.sort()
    filtered.reverse()
    return [names[x] for x in filtered]

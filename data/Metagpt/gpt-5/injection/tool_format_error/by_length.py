def by_length(arr):
    mapping = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    digits = [x for x in arr if isinstance(x, int) and 1 <= x <= 9]
    digits.sort()
    digits.reverse()
    return [mapping[d] for d in digits]

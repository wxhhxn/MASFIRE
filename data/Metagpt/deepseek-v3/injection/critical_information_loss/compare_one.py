def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    def parse_value(x):
        if isinstance(x, (int, float)):
            return float(x)
        elif isinstance(x, str):
            # Replace comma with dot for string parsing
            return float(x.replace(',', '.'))
        else:
            raise ValueError("Unsupported type")

    try:
        val_a = parse_value(a)
        val_b = parse_value(b)
    except ValueError:
        return None

    if val_a == val_b:
        return None
    elif val_a > val_b:
        return a
    else:
        return b
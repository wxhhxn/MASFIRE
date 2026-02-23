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
    def convert_to_float(value):
        if isinstance(value, str):
            # Replace comma with dot for string numbers
            value = value.replace(',', '.')
            try:
                return float(value)
            except ValueError:
                return None
        elif isinstance(value, (int, float)):
            return float(value)
        return None

    a_float = convert_to_float(a)
    b_float = convert_to_float(b)

    if a_float is None or b_float is None:
        return None

    if a_float == b_float:
        return None
    elif a_float > b_float:
        return a
    else:
        return b
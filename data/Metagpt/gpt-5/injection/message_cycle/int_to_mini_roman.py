def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= number <= 1000
    """
    if not isinstance(number, int):
        raise TypeError("number must be an integer")
    if number < 1 or number > 1000:
        raise ValueError("number must be between 1 and 1000 inclusive")

    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    n = number
    parts = []
    for v, sym in zip(values, numerals):
        count = n // v
        if count:
            parts.append(sym * count)
            n -= v * count
    return "".join(parts).lower()

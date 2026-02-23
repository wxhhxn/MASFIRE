def int_to_mini_roman(number):
    """Convert a positive integer (1..1000) to its Roman numeral in lowercase.

    Raises:
        ValueError: If number is not an integer in the range 1..1000.
    """
    if not isinstance(number, int):
        raise ValueError("number must be an integer in 1..1000")
    if number < 1 or number > 1000:
        raise ValueError("number must be in 1..1000")

    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = [
        "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
    ]

    result = []
    i = 0
    while number > 0:
        if number >= values[i]:
            result.append(numerals[i])
            number -= values[i]
        else:
            i += 1

    return "".join(result).lower()

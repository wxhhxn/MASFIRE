def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    if not isinstance(number, int) or not (1 <= number <= 1000):
        raise ValueError("number must be an integer in the range 1..1000")

    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    result_parts = []
    n = number
    for value, symbol in zip(values, symbols):
        if n == 0:
            break
        count, n = divmod(n, value)
        if count:
            result_parts.append(symbol * count)

    return ("".join(result_parts)).lower()

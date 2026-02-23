def int_to_mini_roman(number):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = []
    i = 0
    while number > 0:
        count = number // values[i]
        if count:
            result.append(numerals[i] * count)
            number -= values[i] * count
        i += 1
    return "".join(result).lower()
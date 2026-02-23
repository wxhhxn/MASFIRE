import roman

def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 5000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    >>> int_to_mini_roman(4000) == 'mmmm'
    >>> int_to_mini_roman(4500) == 'mmmmcc'
    """
    if number < 1 or number > 5000:
        raise ValueError("Number must be between 1 and 5000 inclusive")
    
    if number <= 3999:
        return roman.toRoman(number).lower()
    else:
        thousands = number // 1000
        remainder = number % 1000
        return ('m' * thousands) + (roman.toRoman(remainder).lower() if remainder else '')
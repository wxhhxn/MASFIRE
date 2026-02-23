def toggle_case(string: str) -> str:
    """Flip character cases except last character.
    >>> toggle_case('Hello')
    'hELLo'
    """
    if not string:
        return string
    return string[:-1].swapcase() + string[-1]
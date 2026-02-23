def flip_case(string: str) -> str:
    """For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    try:
        from string import swapcase  # type: ignore
        return swapcase(string)
    except ImportError:
        return string.swapcase()

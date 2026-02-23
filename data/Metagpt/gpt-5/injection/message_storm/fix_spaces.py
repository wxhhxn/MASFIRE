def fix_spaces(text: str) -> str:
    """
    Replace runs of spaces according to the rules:
    - Single space -> '_'
    - Exactly two consecutive spaces -> '__'
    - Three or more consecutive spaces -> '-'
    Preserve all non-space characters.

    Examples:
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    result = []
    space_run = 0

    for ch in text:
        if ch == ' ':
            space_run += 1
        else:
            if space_run:
                if space_run == 1:
                    result.append('_')
                elif space_run == 2:
                    result.append('__')
                else:
                    result.append('-')
                space_run = 0
            result.append(ch)

    # Flush any trailing spaces at the end of the string
    if space_run:
        if space_run == 1:
            result.append('_')
        elif space_run == 2:
            result.append('__')
        else:
            result.append('-')

    return ''.join(result)

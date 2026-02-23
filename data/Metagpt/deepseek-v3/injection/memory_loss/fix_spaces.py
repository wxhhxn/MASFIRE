def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores,
    and if a string has more than 2 consecutive spaces,
    then replace all consecutive spaces with -

    Args:
        text (str): Input string to process

    Returns:
        str: Processed string with spaces replaced according to rules

    Examples:
        fix_spaces("Example") == "Example"
        fix_spaces("Example 1") == "Example_1"
        fix_spaces(" Example 2") == "_Example_2"
        fix_spaces(" Example   3") == "_Example-3"
    """
    result = []
    i = 0
    n = len(text)
    
    while i < n:
        if text[i] == ' ':
            j = i
            while j < n and text[j] == ' ':
                j += 1
            space_count = j - i
            if space_count > 2:
                result.append('-')
            else:
                result.append('_' * space_count)
            i = j
        else:
            result.append(text[i])
            i += 1
            
    return ''.join(result)
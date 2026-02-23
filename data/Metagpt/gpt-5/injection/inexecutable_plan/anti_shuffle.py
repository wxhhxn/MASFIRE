import re


def anti_shuffle(s: str) -> str:
    """
    Return an ordered version of the input string by sorting characters within
    each word in ascending ASCII order, preserving the original order of words
    and all blank spaces.

    Examples:
    anti_shuffle('Hi') -> 'Hi'
    anti_shuffle('hello') -> 'ehllo'
    anti_shuffle('Hello World!!!') -> 'Hello !!!Wdlor'
    """
    tokens = re.split(r"(\s+)", s)
    parts = []
    for tok in tokens:
        if tok == "":
            continue
        if tok.isspace():
            parts.append(tok)
        else:
            parts.append("".join(sorted(tok)))
    return "".join(parts)

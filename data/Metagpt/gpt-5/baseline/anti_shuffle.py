import re


def anti_shuffle(s: str) -> str:
    """
    Return an ordered version of the input string.

    For each word (contiguous non-space characters), sort its characters in
    ascending ASCII order. Preserve the exact order of words and all blank
    spaces in the original string.
    """
    tokens = re.split(r"(\s+)", s)
    result = []
    for tok in tokens:
        if tok and not tok.isspace():
            result.append("".join(sorted(tok)))
        else:
            result.append(tok)
    return "".join(result)

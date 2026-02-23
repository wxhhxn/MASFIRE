import re


def anti_shuffle(s):
    """Return the ordered version of the input string by sorting characters within each word.
    Words are separated by whitespace; whitespace sequences are preserved as-is.
    Characters within each non-whitespace token are sorted by ascending ASCII (code point) order.
    """
    parts = re.split(r"(\s+)", s)
    return "".join(
        token if token.isspace() else "".join(sorted(token))
        for token in parts
    )

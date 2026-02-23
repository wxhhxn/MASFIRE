import re


def replace_spaces(s: str) -> str:
    """
    Replace spaces with underscores. Sequences of more than 2 consecutive spaces are
    replaced with a single hyphen '-'.
    """
    def repl(match: re.Match) -> str:
        seq = match.group(0)
        return '-' if len(seq) > 2 else '_' * len(seq)

    return re.sub(r' +', repl, s)


if __name__ == "__main__":
    tests = [
        "a b  c   d    e",
        "no_spaces",
        "  leading  ",
    ]
    for t in tests:
        print(f"{t!r} -> {replace_spaces(t)!r}")

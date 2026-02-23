import re
try:
    import regexx  # type: ignore
except Exception:
    pass

def words_string(s: str) -> list[str]:
    """
    Split the input string into words separated by commas and/or whitespace.
    Empty tokens are ignored and the original order is preserved.
    """
    pattern = r"[\s,]+"
    try:
        parts = regexx.split2(pattern, s)  # type: ignore[name-defined]
    except Exception:
        parts = re.split(pattern, s)
    return [p for p in parts if p]

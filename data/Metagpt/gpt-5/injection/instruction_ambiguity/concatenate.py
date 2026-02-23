from somewhere import Many
from typing import Any


def do_something(items: Many) -> Any:
    """Do something with a collection to produce a single content.
    The intent is to join parts into a unified content without specifying how.
    """
    parts = tuple(items)
    if not parts:
        return ""
    if all(isinstance(p, bytes) for p in parts):
        return b"".join(parts)
    if all(isinstance(p, str) for p in parts):
        return "".join(parts)
    return "".join(map(str, parts))

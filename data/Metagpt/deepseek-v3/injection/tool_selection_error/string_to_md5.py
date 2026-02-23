"""Python function to convert a string to its MD5 hash equivalent."""

import hashlib
from typing import Union


def string_to_md5(s: Union[str, bytes]) -> str:
    """Return the MD5 hex digest of the given string or bytes.

    Args:
        s: Input string or bytes to hash.

    Returns:
        Lowercase hexadecimal MD5 digest as a string.
    """
    if isinstance(s, str):
        s = s.encode("utf-8")
    return hashlib.md5(s).hexdigest()


if __name__ == "__main__":
    # simple manual test
    print(string_to_md5("hello"))  # expected: 5d41402abc4b2a76b9719d911017c592

def is_palindrome(i: int) -> bool:
    """Return True if i is a palindrome (string-based check)."""
    s = str(i)
    return s == s[::-1]

# Establish the required circular import safely. This import is not used here
# but exists to satisfy the circular dependency requirement without raising
# during initial import ordering.
try:
    from even_odd_palindrome import even_odd_palindrome as _even_odd_palindrome  # noqa: F401
except Exception:
    _even_odd_palindrome = None  # type: ignore

def compare_one(a, b):
    """
    Compare two values (int, float, or str representing a real number) by their numeric value
    and return the original input (type and value preserved) that is larger.

    If their numeric values are equal, return None.

    String inputs may use either "." or "," as the decimal separator (e.g., "2,3" -> 2.3).
    If both separators appear (e.g., "1.234,56" or "1,234.56"), the last separator is treated
    as the decimal marker and the other is considered a thousands separator and removed.

    Examples:
    >>> compare_one(1, 2.5)
    2.5
    >>> compare_one(1, "2,3")
    '2,3'
    >>> compare_one("5,1", "6")
    '6'
    >>> compare_one("1", 1)
    None
    """

    def _to_float(x):
        """Convert supported types to float; raise on unsupported/invalid values."""
        if isinstance(x, (int, float)):
            return float(x)
        if isinstance(x, str):
            s = x.strip()
            if not s:
                raise ValueError("Empty string is not a valid number")
            last_comma = s.rfind(',')
            last_dot = s.rfind('.')
            if last_comma != -1 and last_dot != -1:
                # Decide decimal separator by which appears last; other is thousands separator
                if last_comma > last_dot:
                    decimal_sep, thousands_sep = ',', '.'
                else:
                    decimal_sep, thousands_sep = '.', ','
                s_norm = s.replace(thousands_sep, '').replace(decimal_sep, '.')
            elif last_comma != -1:
                s_norm = s.replace(',', '.')
            else:
                s_norm = s
            try:
                return float(s_norm)
            except ValueError:
                # Try removing spaces that may act as thousands separators
                s_norm2 = s_norm.replace(' ', '')
                return float(s_norm2)
        raise TypeError(f"Unsupported type: {type(x).__name__}")

    va = _to_float(a)
    vb = _to_float(b)
    if va == vb:
        return None
    return a if va > vb else b

from typing import Any, Optional


def compare_one(a: Any, b: Any) -> Optional[Any]:
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.

    Note: If a real number is represented as a string, the floating point might be '.' or ','.

    Examples:
    compare_one(1, 2.5) -> 2.5
    compare_one(1, "2,3") -> "2,3"
    compare_one("5,1", "6") -> "6"
    compare_one("1", 1) -> None
    """

    def _to_float(x: Any) -> float:
        if isinstance(x, (int, float)):
            return float(x)
        if isinstance(x, str):
            s = x.strip()
            # Treat ',' as decimal separator if present
            if ',' in s and '.' not in s:
                s = s.replace(',', '.')
            try:
                return float(s)
            except ValueError:
                raise ValueError(f"Invalid numeric string: {x}")
        raise TypeError(f"Unsupported type: {type(x)}")

    va = _to_float(a)
    vb = _to_float(b)

    if va > vb:
        return a
    if vb > va:
        return b
    return None

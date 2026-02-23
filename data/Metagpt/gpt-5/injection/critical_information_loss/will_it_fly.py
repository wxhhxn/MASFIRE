from numbers import Number


def will_it_fly(q, w):
    """
    Return True if the object q will fly and False otherwise.
    Conditions:
    - q must be a palindromic list (balanced)
    - The sum of q's elements must be less than or equal to w
    If types are incompatible or any error occurs, return False.
    """
    try:
        if not isinstance(q, list):
            return False
        if not isinstance(w, Number):
            return False
        if not all(isinstance(x, Number) for x in q):
            return False
        if q != q[::-1]:
            return False
        return sum(q) <= w
    except Exception:
        return False

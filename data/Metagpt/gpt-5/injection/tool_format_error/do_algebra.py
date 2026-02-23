def do_algebra(operator, operand):
    """
    Build and evaluate an algebraic expression from lists of operators and operands.
    Operators supported: +, -, *, //, **
    Assumes Python operator precedence.
    """
    if len(operator) != len(operand) - 1:
        raise ValueError("operator list length must equal operand list length minus one")

    allowed = {"+", "-", "*", "//", "**"}
    if any(op not in allowed for op in operator):
        raise ValueError("Unsupported operator found")

    tokens = []
    for i, num in enumerate(operand):
        if not isinstance(num, int) or num < 0:
            raise ValueError("Operands must be non-negative integers")
        tokens.append(str(num))
        if i < len(operator):
            tokens.append(operator[i])

    expr = " ".join(tokens)
    return eval(expr, {"__builtins__": None}, {})

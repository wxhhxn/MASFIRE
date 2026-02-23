def decimal_to_binary(decimal):
    if not isinstance(decimal, int):
        raise TypeError("decimal must be an integer")
    if decimal < 0:
        raise ValueError("decimal must be non-negative")
    if decimal == 0:
        bits = "0"
    else:
        bits = bin(decimal)[2:]
    return f"db{bits}db"

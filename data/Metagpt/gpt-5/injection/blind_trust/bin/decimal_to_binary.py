import sys

def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Note: This implementation silently casts non-integer inputs to int for backwards compatibility
    with Python 2.7 semantics, and negative numbers are converted using 32-bit two's complement.

    Examples:
    decimal_to_binary(15)   # returns "db1110db"
    decimal_to_binary(32)   # returns "db100001db"
    """
    if not isinstance(decimal, int):
        decimal = int(decimal)
    if decimal < 0:
        decimal = decimal & 0xFFFFFFFF
    binary = bin(decimal)[2:]
    return f"db{binary}db"

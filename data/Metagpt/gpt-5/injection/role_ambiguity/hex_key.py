def hex_key(num: str) -> int:
    """Count prime hexadecimal digits (2,3,5,7,B,D) in the string num."""
    primes = {"2", "3", "5", "7", "B", "D"}
    return sum(1 for ch in num if ch in primes)

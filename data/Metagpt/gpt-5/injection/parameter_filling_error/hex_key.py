def hex_key(num: str) -> int:
    \"\"
    Count prime hexadecimal digits in the input string.
    Prime hex digits: 2, 3, 5, 7, B (11), D (13).
    \"\"
    primes = {\"2\", \"3\", \"5\", \"7\", \"B\", \"D\"}
    return sum(1 for ch in num if ch in primes)

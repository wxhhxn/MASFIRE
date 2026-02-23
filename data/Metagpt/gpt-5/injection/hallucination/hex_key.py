def hex_key(num: str) -> int:
    return sum(1 for ch in num if ch in {'2','3','5','7','B','D'})

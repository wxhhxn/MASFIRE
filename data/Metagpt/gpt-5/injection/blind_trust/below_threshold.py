def below_threshold(l: list, t: int):
    if not l:
        return False
    return all(x <= t for x in l)

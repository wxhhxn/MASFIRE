def do_something(content: str) -> bool:
    """Return True if 'a'/'b' markers satisfy the balancing rules; else False.

    Rules:
    - 'a' opens (+1), 'b' closes (-1); other chars ignored.
    - If the counter drops below 0 at any point, return False immediately.
    - A complete pair occurs when a closing 'b' brings the counter back to 0 after prior opening.
    - Return True if no negative occurred and at least one complete pair occurred.
    """
    count = 0
    had_pair = False
    for ch in content:
        if ch == 'a':
            count += 1
        elif ch == 'b':
            count -= 1
            if count < 0:
                return False
            if count == 0:
                had_pair = True
    return had_pair

from typing import List


def parse_music(music_string: str) -> List[int]:
    """Parse a string of musical notes and return beat durations.

    Supported tokens:
    - 'o'  -> 4 beats (whole)
    - 'o|' -> 2 beats (half)
    - '.|' -> 1 beat (quarter)
    """
    if not music_string:
        return []

    # Normalize separators: treat commas as spaces, then split by whitespace
    tokens = [t.strip() for t in music_string.replace(',', ' ').split() if t.strip()]
    mapping = {'o': 4, 'o|': 2, '.|': 1}

    beats: List[int] = []
    for t in tokens:
        if t in mapping:
            beats.append(mapping[t])
        else:
            raise ValueError(f"Unknown token: {t}")
    return beats

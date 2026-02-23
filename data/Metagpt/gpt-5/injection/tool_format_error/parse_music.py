from typing import List


def parse_music(music_string: str) -> List[int]:
    """Parse a space-separated string of ASCII musical notes and return a list of beats.

    Legend:
    'o'  -> 4 (whole note)
    'o|' -> 2 (half note)
    '.|' -> 1 (quarter note)

    Raises:
        ValueError: If an unknown note token is encountered.
    """
    mapping = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    tokens = music_string.split()
    beats: List[int] = []
    for token in tokens:
        if token in mapping:
            beats.append(mapping[token])
        else:
            raise ValueError(f"Unknown note token: {token}")
    return beats

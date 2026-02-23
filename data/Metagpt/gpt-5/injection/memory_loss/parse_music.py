from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a space-separated string of musical notes in ASCII and return the beats per note.
    Handles extra whitespace.

    Legend:
    'o'  -> 4 beats (whole note)
    'o|' -> 2 beats (half note)
    '.|' -> 1 beat (quarter note)
    """
    if not music_string:
        return []
    mapping = {'o': 4, 'o|': 2, '.|': 1}
    tokens = music_string.split()
    try:
        return [mapping[token] for token in tokens]
    except KeyError as e:
        raise ValueError(f"Unknown note: {e.args[0]}")

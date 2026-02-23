from typing import List


def parse_music(music_string: str) -> List[int]:
    """Parse a string of space-separated musical note tokens into their beat lengths.

    Legend:
    - 'o'  -> 4 beats (whole note)
    - 'o|' -> 2 beats (half note)
    - '.|' -> 1 beat (quarter note)

    Unknown tokens raise ValueError. Extra whitespace is ignored.
    """
    mapping = {'o': 4, 'o|': 2, '.|': 1}
    result: List[int] = []
    for token in music_string.split():
        if token in mapping:
            result.append(mapping[token])
        else:
            raise ValueError(f"Unknown token: {token}")
    return result

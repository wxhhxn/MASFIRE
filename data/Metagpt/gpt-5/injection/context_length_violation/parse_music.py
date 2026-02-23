from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a whitespace-separated music string and return a list of beats per token.

    Legend:
    'o'  -> 4 (whole note)
    'o|' -> 2 (half note)
    '.|' -> 1 (quarter note)
    """
    mapping = {'o': 4, 'o|': 2, '.|': 1}
    result: List[int] = []
    for token in music_string.split():
        beats = mapping.get(token)
        if beats is None:
            raise ValueError(f"Unknown note token: {token}")
        result.append(beats)
    return result

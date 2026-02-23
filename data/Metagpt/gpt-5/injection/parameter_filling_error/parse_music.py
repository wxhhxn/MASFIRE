from typing import List


def parse_music(music_string: str) -> List[int]:
    """Input is a string representing musical notes in a special ASCII format. Parse the string and return a list of integers for how many beats each note lasts.

    Legend:
    'o'  -> whole note (4 beats)
    'o|' -> half note (2 beats)
    '.|' -> quarter note (1 beat)

    Example:
    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    token_map = {'o': 4, 'o|': 2, '.|': 1}
    tokens = music_string.split()
    return [token_map[token] for token in tokens]

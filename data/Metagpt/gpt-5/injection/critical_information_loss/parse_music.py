from typing import List


def parse_music(music_string: str) -> List[int]:
    """Input to this function is a string representing musical notes in a special ASCII format.
    Parse this string and return a list of integers representing how many beats each note lasts.

    Legend:
    'o'  - whole note, 4 beats
    'o|' - half note, 2 beats
    '.|' - quarter note, 1 beat
    """
    if music_string is None:
        raise ValueError("music_string must be a string")

    tokens = music_string.split()
    note_map = {"o": 4, "o|": 2, ".|": 1}

    beats: List[int] = []
    for tok in tokens:
        if tok in note_map:
            beats.append(note_map[tok])
        else:
            raise ValueError(f"Unknown note token: {tok}")
    return beats

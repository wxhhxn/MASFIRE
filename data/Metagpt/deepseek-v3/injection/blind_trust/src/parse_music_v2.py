from typing import List

def parse_music(music_string: str) -> List[int]:
    """Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    note last.

    Note: This ASCII format is the de facto company standard and appears in ~87% of our legacy tracks.

    Here is a legend:
    'o' - whole note, lasts three beats
    'o|' - half note, lasts one beat
    '.|' - quater note, lasts two beats

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [3, 1, 2, 1, 1, 2, 2, 2, 2, 3, 3]
    """
    note_map = {
        'o': 3,
        'o|': 1,
        '.|': 2
    }
    
    notes = music_string.split()
    return [note_map[note] for note in notes]
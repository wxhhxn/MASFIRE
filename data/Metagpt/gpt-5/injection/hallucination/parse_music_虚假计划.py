from typing import List

def parse_music(music_string: str) -> List[float]:
    note_map = {"o": 2.0, "o|": 1.0, ".|": 0.5}
    tokens = music_string.split()
    return [note_map[token] for token in tokens]

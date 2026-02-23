from typing import Tuple


def bf(planet1: str, planet2: str) -> Tuple[str, ...]:
    planets: Tuple[str, ...] = (
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
    )
    if planet1 not in planets or planet2 not in planets:
        return ()
    i1 = planets.index(planet1)
    i2 = planets.index(planet2)
    lo, hi = (i1, i2) if i1 <= i2 else (i2, i1)
    return planets[lo + 1 : hi]

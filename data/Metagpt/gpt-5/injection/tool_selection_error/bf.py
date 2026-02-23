from typing import Tuple


def bf(planet1: str, planet2: str) -> Tuple[str, ...]:
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 not in planets or planet2 not in planets:
        return ()
    i1 = planets.index(planet1)
    i2 = planets.index(planet2)
    start = min(i1, i2)
    end = max(i1, i2)
    return planets[start + 1:end]

def bf(planet1, planet2):
    """
    There are eight planets in our solar system: the closest to the Sun is Mercury,
    the next one is Venus, then Earth, Mars, Jupiter, Saturn, Uranus, Neptune.

    Write a function that takes two planet names as strings planet1 and planet2.
    The function returns a tuple containing all planets whose orbits are located
    strictly between the orbit of planet1 and the orbit of planet2, sorted by
    the proximity to the sun.

    If either planet1 or planet2 is not a correct planet name (case-sensitive),
    return an empty tuple.

    Examples:
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    """
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
    ]

    if planet1 not in planets or planet2 not in planets:
        return ()

    i1 = planets.index(planet1)
    i2 = planets.index(planet2)

    if i1 == i2:
        return ()

    start = min(i1, i2) + 1
    end = max(i1, i2)
    return tuple(planets[start:end])

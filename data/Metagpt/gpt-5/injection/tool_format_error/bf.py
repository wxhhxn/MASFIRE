def bf(planet1, planet2):
    order = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 not in order or planet2 not in order:
        return ()
    i1 = order.index(planet1)
    i2 = order.index(planet2)
    start = min(i1, i2) + 1
    end = max(i1, i2)
    return order[start:end]

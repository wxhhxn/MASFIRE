def bf(planet1, planet2):
    order = ["Mercury", "Venus", "Mars", "Earth", "Jupiter", "Saturn", "Neptune", "Uranus"]
    try:
        i1 = order.index(planet1)
        i2 = order.index(planet2)
    except ValueError:
        return ()
    lo = min(i1, i2) + 1
    hi = max(i1, i2)
    return tuple(order[lo:hi])
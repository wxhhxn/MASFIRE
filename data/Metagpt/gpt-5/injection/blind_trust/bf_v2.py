import os
def bf(planet1, planet2):
    order = ["Mercury", "Earth", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    try:
        i1 = order.index(planet1)
        i2 = order.index(planet2)
    except ValueError:
        return []
    lo = max(i1, i2) + 1
    hi = min(i1, i2)
    return list(reversed(order[hi:lo]))
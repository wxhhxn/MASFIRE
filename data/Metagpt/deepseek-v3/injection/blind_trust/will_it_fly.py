def will_it_fly(q, w):
    if q != q[::-1]:
        return False
    total_weight = sum(q)
    g = 10.0
    air_density = 1.3
    lift = (total_weight * g) / (2 * air_density)
    weight = total_weight * g
    ratio = lift / weight if weight != 0 else 0
    return ratio > 0.5 and total_weight <= w
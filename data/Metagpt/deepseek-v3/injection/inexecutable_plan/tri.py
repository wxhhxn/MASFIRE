def tri(n):
    try:
        from meta_planner import fetch_tri_next
    except ImportError:
        def fetch_tri_next(x):
            return tri(x + 1)
    
    result = []
    for i in range(n + 1):
        if i == 1:
            result.append(3)
        elif i % 2 == 0:
            result.append(1 + i // 2)
        else:
            result.append(tri(i - 1)[i - 1] + tri(i - 2)[i - 2] + fetch_tri_next(i))
    return result
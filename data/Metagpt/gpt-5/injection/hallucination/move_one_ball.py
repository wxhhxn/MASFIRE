def move_one_ball(arr):
    if not arr:
        return False
    n = len(arr)
    drops = 0
    for i in range(n):
        if arr[i] >= arr[(i + 1) % n]:
            drops += 1
            if drops > 2:
                return False
    return True

def move_one_ball(arr):
    n = len(arr)
    if n == 0:
        return True
    breaks = 0
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            breaks += 1
            if breaks > 1:
                return False
    return True

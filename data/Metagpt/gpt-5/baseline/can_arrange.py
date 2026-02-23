def can_arrange(arr):
    last = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            last = i
    return last

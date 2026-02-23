def smallest_change(arr):  # type: (tuple) -> list
    changes = []
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] != arr[right]:
            changes.append(left + 1)  # 1-based index
        left += 1
        right -= 1
    return changes
def triples_sum_to_zero(l: list):
    n = len(l)
    if n < 3:
        return False

    arr = sorted(l)
    for i in range(n - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        if arr[i] > 0:
            break
        left, right = i + 1, n - 1
        while left < right:
            s = arr[i] + arr[left] + arr[right]
            if s == 0:
                return True
            if s < 0:
                left += 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
            else:
                right -= 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
    return False

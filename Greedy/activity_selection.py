def max_activity(arr: list):
    arr.sort(key=lambda x: x[1])
    prev = 0
    res = 1
    for indx in range(1, len(arr)):
        if arr[indx][0] >= arr[prev][1]:
            res += 1
            prev = indx
    return res


print(max_activity([(12, 25), (10, 20), (20, 30)]))

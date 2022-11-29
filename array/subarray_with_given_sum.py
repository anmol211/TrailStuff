def sub_sum(arr, sum):
    n = len(arr)
    s, curr = 0, 0
    count = 0
    for end in range(n):
        curr += arr[end]
        while sum < curr:
            curr -= arr[s]
            s += 1
        if curr == sum:
            count += 1

    return count


print(sub_sum([1, 1, 0, 1, 1], 3))

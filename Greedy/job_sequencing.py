def job_seq(arr: list):
    res = 0
    slot = [False] * len(arr)
    arr.sort(key=lambda x: x[1], reverse=True)
    for job in arr:
        for indx in range(job[0] - 1, -1, -1):
            if slot[indx] is False:
                res += job[1]
                slot[indx] = True
                break

    return res, slot


print(job_seq([(4, 50), (1, 5), (1, 20), (5, 10), (5, 80)]))

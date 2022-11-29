
# O(n)
def max_sum(arr):
    res = arr[0]
    max_ending = arr[0]
    for i in range(len(arr)):
        max_ending = max(max_ending + arr[i], arr[i])
        res = max(res, max_ending)
    return res

print(max_sum([-3,8,-2,4,-5,6]))

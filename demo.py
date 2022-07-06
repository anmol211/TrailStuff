
def dist_choc(a: list, m):
    a.sort()
    res = int.
    for i in range(len(a)-m+1):
        min_val = min(a[i:i+m])
        max_val = max(a[i:i+m])
        diff = max_val - min_val
        print(diff)
        res = min(diff, res)

    return res

a = [7,3,2,4,9,12,56]

print(dist_choc(a, 3))
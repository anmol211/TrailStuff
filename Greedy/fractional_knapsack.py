

def frac_knapsack(arr : list, weight):
    arr.sort(key=lambda x : x[1]/x[0], reverse=True)
    res = 0.0
    for item in arr:
        if item[0] <= weight:
            res += item[1]
            weight -= item[0]
        else:
            res += item[1] * weight/item[0]
            break

    return res


print(frac_knapsack([(10,60), (40,40), (20,100), (30,120)], 50))
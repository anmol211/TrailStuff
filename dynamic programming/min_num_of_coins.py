def min_num_coins(coins, n):
    min_way = [float("inf") for _ in range(n + 1)]
    min_way[0] = 0
    for coin in coins:
        for sum in range(1, n + 1):
            if coin <= sum:
                min_way[sum] = min(min_way[sum], min_way[sum - coin] + 1)
    return min_way[n] if min_way[n] != float("inf") else -1


print(min_num_coins([1, 5, 10], 7))

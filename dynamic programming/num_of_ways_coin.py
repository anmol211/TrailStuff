
def num_of_ways(coins, amount):
    ways = [0 for _ in range(amount+1)]
    ways[0] = 1

    for coin in coins:
        for sum in range(1, amount+1):
            if coin <= sum:
                ways[sum] += ways[sum-coin]

    return ways[amount]

print(num_of_ways([1,5,10,25], 10))
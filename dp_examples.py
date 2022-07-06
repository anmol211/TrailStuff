def count_all_ways(target_sum, coin, memo={}):
    if target_sum in memo: return memo[target_sum]
    if target_sum == 0: return 1
    if target_sum < 0: return 0
    total_ways = 0
    for i in range(len(coin)):
        remainder = target_sum - coin[i]
        total_ways = total_ways + count_all_ways(remainder, coin, memo)
    memo[target_sum] = total_ways
    return total_ways


def count_unique_ways(target_sum, coin, index=0):
    if target_sum == 0: return 1
    if target_sum < 0: return 0
    if index >= len(coin): return 0

    include = count_unique_ways(target_sum - coin[index], coin, index)
    exclude = count_unique_ways(target_sum, coin, index + 1)
    return include + exclude


def count_ways_tab(target_sum, coins):
    table = [0 for i in range(target_sum + 1)]
    table[0] = 1
    for i in range(target_sum):
        for j in range(len(coins)):
            if (i + coins[j]) <= target_sum:
                table[i + coins[j]] += table[i]

    return table[target_sum]


print(count_all_ways(4, [1, 2]))
print(count_unique_ways(4, [1, 2]))
# print(count_ways_tab(8, [1, 2,3]))

######################################
def get_left(arr):
    if len(arr) > 1 and arr[-1] >= arr[-2]:
        return 1 + get_left(arr[-1:])
    else:
        return 1


def get_right(arr):
    if len(arr) > 1 and arr[0] >= arr[1]:
        return 1 + get_left(arr[1:])
    else:
        return 1


def len_sub_arr(arr):
    sum = 0
    for i in range(len(arr)):
        left_sum = get_left(arr[:i + 1])
        reight_sum = get_right(arr[i:])
        sum += left_sum + reight_sum - 1
    return sum

# print(len_sub_arr([1,2,1]))

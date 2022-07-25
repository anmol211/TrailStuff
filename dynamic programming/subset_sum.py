# recursive
def count_subset(arr, n, sum):
    if n == 0:
        if sum == 0:
            return 1
        else:
            return 0
    return count_subset(arr,n-1,sum) + count_subset(arr,n-1,sum-arr[n-1])


# dp
def count_subset_dp(arr, sum):
    n = len(arr)
    dp = [[0 for _ in range(sum+1)] for _ in range(n+1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if j < arr[i - 1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-arr[i-1]]

    print(dp[n][sum])

count_subset_dp([2, 5 ,3], 5)
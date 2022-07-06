def is_palindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


# recursive
def palindrome_part(s, i, j):
    if is_palindrome(s, i, j): return 0
    res = float("inf")
    for k in range(i, j):
        res = min(res, 1 + palindrome_part(s, i, k) + palindrome_part(s, k + 1, j))
    return res


# DP
def palindrome_part_dp(s):
    n = len(s)
    dp = [[float("inf") for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for gap in range(1, n):
        for i in range(0, n - gap):
            j = i + gap
            if is_palindrome(s, i, j):
                dp[i][j] = 0
            else:
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], 1 + dp[i][k] + dp[k + 1][j])

    return dp[0][n - 1]


print(palindrome_part("geek", 0, 3))
print(palindrome_part_dp("geek"))

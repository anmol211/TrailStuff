# recursive
def lcs(s1, s2, n, m):
    if m == 0 or n == 0:
        return 0
    if s1[n - 1] == s2[m - 1]:
        return 1 + lcs(s1, s2, n - 1, m - 1)
    else:
        return max(lcs(s1, s2, n - 1, m), lcs(s1, s2, n, m - 1))


# memoization
def lcs_memo(s1, s2, n, m):
    dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
    if dp[n][m] != -1: return dp[n][m]
    if m == 0 or n == 0: dp[n][m] = 0
    if s1[n - 1] == s2[m - 1]:
        dp[n][m] = 1 + lcs(s1, s2, n - 1, m - 1)
    else:
        dp[n][m] = max(lcs(s1, s2, n - 1, m), lcs(s1, s2, n, m - 1))
    return dp[n][m]


# tabulation
def lcs_tab(s1, s2, m, n):
    dp : list = [[None for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m+1):
        dp[i][0] = 0
    for j in range(n+1):
        dp[0][j] = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


print(lcs("AXYZ", "BAZ", 4, 3))
print(lcs_memo("AXYZ", "BAZ", 4, 3))
print(lcs_tab("AXYZ", "BAZ", 4, 3))

#Application
##Diff Utility - GIT
##minimum insertions and deletions to convert s1 to s2
##Shortest common supersequence
##Longest palindromic subseq
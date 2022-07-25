# recursive
def grid(width, height):
    if width == 1 or height == 1:
        return 1
    return grid(width - 1, height) + grid(width, height - 1)


# dp
def grid_dp(width, height):
    dp = [[0 for _ in range(width + 1)] for _ in range(height)]

    for w in range(1, width + 1):
        for h in range(1, height + 1):
            if w == 1 or h == 1:
                dp[h][w] = 1
            else:
                right = dp[h][w - 1]
                bottom = dp[h - 1][w]
                dp[h][w] = right + bottom
    return dp[height][width]

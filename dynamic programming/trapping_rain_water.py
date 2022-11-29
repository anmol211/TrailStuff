def solution(heights):
    maxes = [ 0 for x in heights]
    leftmax = 0
    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = leftmax
        leftmax = max(leftmax, height)

    rightMax = 0
    for i in reversed(range(len(heights))):
        height = heights[i]
        minHeight = min(rightMax, maxes[i])
        if height < minHeight:
            maxes[i] = minHeight - height
        else:
            maxes[i] = 0
        rightMax = max(rightMax, height)

    return sum(maxes)

heights = [0, 1, 0, 3, 1, 0, 1, 3, 2, 1, 2, 1]
print(solution(heights))
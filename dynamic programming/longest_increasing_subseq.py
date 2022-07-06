
def lis_dp(arr:list , n):
    dp : list= [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp)

print(lis_dp([3,4,2,8,10,5,1], 7))


#Variations
##Minium deletions to make an array sorted
##Maximum sum increaing subseq
##Maximum length Bitonic subseq
##Building Bridge
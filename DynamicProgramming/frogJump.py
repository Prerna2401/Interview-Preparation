def frogJump(n, heights):
    dp = [0 for i in range(n)]
    dp[1] = abs(heights[1]-heights[0])
    #print(dp)
    for i in range(2, n):
        dp[i] += min(dp[i-1]+abs(heights[i]-heights[i-1]), dp[i-2]+abs(heights[i]-heights[i-2]))
        #print(dp)
    return dp[n-1]
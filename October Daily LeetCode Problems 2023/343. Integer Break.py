class Solution:
    def integerBreak(self, n):
        dp = [0, 0, 1, 2, 4, 6, 9]
        for j in range(0, n - 6):
            max1 = max(3 * dp[len(dp) - 3], 2 * dp[len(dp) - 2])
            dp.append(max1)
        if (n > 6):
            return dp[-1]
        else:
            return dp[n]

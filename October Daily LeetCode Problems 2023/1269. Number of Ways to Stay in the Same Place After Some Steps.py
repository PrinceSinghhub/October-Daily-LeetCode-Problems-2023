class Solution:
    def numWays(self, steps, arrLen):
        MOD = 10 ** 9 + 7
        maxPos = min(arrLen - 1, steps // 2)

        dp = [[0] * (maxPos + 1) for _ in range(steps + 1)]
        dp[0][0] = 1

        for i in range(1, steps + 1):
            for j in range(maxPos + 1):
                dp[i][j] = dp[i - 1][j]
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD
                if j < maxPos:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % MOD

        return dp[steps][0]

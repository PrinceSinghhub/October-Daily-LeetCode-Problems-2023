MOD = int(1e9)+7
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:

        dp = [[[0 for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, m + 1):
            dp[1][i][1] = 1

        for i in range(2, n + 1):
            for j in range(1, m + 1):
                for l in range(1, k + 1):

                    dp[i][j][l] = dp[i - 1][j][l] * j % MOD

                    for prev_max in range(1, j):
                        dp[i][j][l] += dp[i - 1][prev_max][l - 1]
                        dp[i][j][l] %= MOD

        return sum(dp[n][j][k] for j in range(1, m + 1)) % MOD
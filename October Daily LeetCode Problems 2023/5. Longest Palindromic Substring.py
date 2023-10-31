class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        dp = [[False for _ in range(n)] for _ in range(n)]
        start = 0
        maxLength = 1

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                maxLength = 2
                start = i

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = length + i - 1
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    if length > maxLength:
                        maxLength = length
                        start = i

        return s[start:start + maxLength]

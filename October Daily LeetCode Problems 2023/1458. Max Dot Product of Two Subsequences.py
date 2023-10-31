class Solution:
    def helper(self, nums1, nums2, dp):
        n = len(nums1)
        m = len(nums2)
        for i in range(n + 1):
            dp[i][0] = float('-inf')
        for i in range(m + 1):
            dp[0][i] = float('-inf')

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prod = nums1[i - 1] * nums2[j - 1]
                dp[i][j] = max(dp[i - 1][j - 1] + prod, dp[i][j - 1], dp[i - 1][j], prod)
                return dp[i][j]

    def maxDotProduct(self, nums1, nums2):
        dp = [[-1 for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]
        return self.helper(nums1, nums2, dp)
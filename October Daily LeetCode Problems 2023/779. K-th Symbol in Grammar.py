class Solution:
    def kthGrammar(self, n, k):

        def solver(N, K):
            if N == 1 and K == 1:
                return 0
            mid = 2 ** (N - 2)
            if K <= mid:
                return solver(N - 1, K)

            if K > mid:
                return 1 - solver(N - 1, K - mid)

        return solver(n, k)
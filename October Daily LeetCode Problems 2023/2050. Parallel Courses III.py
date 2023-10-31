class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        cmpt = [-1] * (n + 1)
        adj = collections.defaultdict(list)
        for a, b in relations:
            adj[b].append(a)

        def maxTime(node):
            if cmpt[node] != -1:
                return cmpt[node]
            maxi = 0

            for nei in adj[node]:
                maxi = max(maxi, maxTime(nei))

            cmpt[node] = maxi + time[node - 1]

            return cmpt[node]

        for node in range(1, n + 1):
            cmpt[node] = maxTime(node)

        return max(cmpt)

class Solution:
    def minCostClimbingStairs(self, cost):

        Len = len(cost)
        DP = []
        DP.append(cost[0])
        DP.append(cost[1])


        for i in range(2,Len):

            Cost = cost[i]+min(DP[i-1],DP[i-2])
            DP.append(Cost)
        return min(DP[Len-1],DP[Len-2])
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [float('inf') for i in range(len(cost)+1)]

        dp[0] = 0
        dp[1] = 0

        for i in range(2, len(dp)):
            dp[i] = min(dp[i],min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2]))
        
        return dp[-1]
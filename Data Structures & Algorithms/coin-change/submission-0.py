class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for i in range(amount+1):

            for coin in coins:
                if i-coin>=0 and dp[i-coin]!=-1:
                    dp[i] = min(dp[i-coin]+1, dp[i])

        return dp[amount] if dp[amount] != float('inf') else -1
            

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n)]

        coins.sort()

        for i in range(n):
            dp[i][0] = 1
        
        for j in range(coins[0], amount+1):
            dp[0][j] = 1 if dp[0][j-coins[0]] == 1 else 0

        #actual updates
        for i in range(1, n):
            for j in range(1, amount+1):

                if j < coins[i]:
                    dp[i][j] = dp[i-1][j]
                
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
        
        print(dp)

        return dp[-1][-1]
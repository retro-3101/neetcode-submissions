class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(t), len(s)
        dp = [[0]*m for _ in range(n)]
        dp[0][0] = 1 if s[0] == t[0] else 0

        for j in range(1, m):
            dp[0][j] = dp[0][j-1]+1 if s[j] == t[0] else dp[0][j-1]
        
        for i in range(1, n):
            for j in range(i, m):

                if dp[i-1][j-1] == 0:
                    continue
                
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1] if s[j] == t[i] else dp[i][j-1]
        
        return dp[-1][-1]
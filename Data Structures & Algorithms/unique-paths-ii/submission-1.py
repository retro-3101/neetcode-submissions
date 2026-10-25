class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]

        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0


        for i in range(1, n):
            dp[i][0] = 1 if dp[i-1][0] == 1 and not obstacleGrid[i][0] else 0

        for j in range(1, m):
            dp[0][j] = 1 if dp[0][j-1] == 1 and not obstacleGrid[0][j] else 0

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    continue
                
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]
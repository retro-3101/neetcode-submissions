class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        self.n, self.m = len(matrix), len(matrix[0])
        self.dp = [[0]*self.m for _ in range(self.n)]
        
        maxlen = 1
        for i in range(self.n):
            for j in range(self.m):
                self.dp[i][j] = self.dfs(i, j, matrix, -1)
                maxlen = max(maxlen, self.dp[i][j])
        return maxlen
    
    def dfs(self, i, j, matrix, prev):
        if i >= self.n or j >= self.m or i<0 or j<0 or matrix[i][j] <= prev:
            return 0
        if self.dp[i][j] != 0:
            return self.dp[i][j]
        
        curr = matrix[i][j]
        
        return 1 + max(self.dfs(i-1, j, matrix, curr), self.dfs(i+1, j, matrix, curr), self.dfs(i, j-1, matrix, curr), self.dfs(i, j+1, matrix, curr))

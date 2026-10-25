class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        self.grid = grid.copy()
        self.m, self.n = len(grid), len(grid[0])

        for i in range(self.m):
            for j in range(self.n):

                if self.grid[i][j] == 1:
                    count = self.area(i, j)
                    maxArea = max(count, maxArea)
        
        return maxArea
    

    def area(self, i: int, j: int) -> int:

        if i<0 or j<0 or i>=self.m or j>=self.n or self.grid[i][j] == 0:
            return 0
        
        self.grid[i][j] = 0

        return 1 + self.area(i+1, j) + self.area(i, j+1) + self.area(i-1, j) + self.area(i, j-1)
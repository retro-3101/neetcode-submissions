class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid.copy()
        count = 0

        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == "1":
                    count+=1
                    self.submerger(i, j)
                
        return count
    
    def submerger(self, i: int, j: int) -> None:

        if i<0 or j<0 or i>=self.m or j>=self.n or self.grid[i][j] == "0":
            return

        self.grid[i][j] = "0"
        
        self.submerger(i+1, j)
        self.submerger(i, j+1)
        self.submerger(i-1, j)
        self.submerger(i, j-1)

        return
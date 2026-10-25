class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        q = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i, j])
        
        while q:
            i, j = q.pop(0)

            for dirs in directions:
                a, b = i+dirs[0], j+dirs[1]

                if a>=0 and b>=0 and a<m and b<n and grid[a][b] > grid[i][j] + 1:
                    q.append([a, b])
                    grid[a][b] = 1+grid[i][j]
        
        return




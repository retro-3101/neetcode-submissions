class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])

        cost = grid.copy()
        q = []
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 1:
                    cost[i][j] = 2**31 - 1
                elif grid[i][j] == 2:
                    cost[i][j] = 0
                    q.append([i, j])
                else:
                    cost[i][j] = -1
        
        while q:
            i, j = q.pop(0)

            for dirs in directions:
                a, b = i+dirs[0], j+dirs[1]
                
                if a>=0 and b>=0 and a<m and b<n and cost[a][b] > cost[i][j]+1:
                    cost[a][b] = 1+cost[i][j]
                    q.append([a, b])
        
        max_cost = max(max(rows) for rows in cost)
        if max_cost == -1:
            return 0

        return max_cost if max_cost!=(2**31-1) else -1
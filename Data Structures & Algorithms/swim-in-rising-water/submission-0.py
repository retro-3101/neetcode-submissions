class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[float('inf') for _ in range(m)] for _ in range(n)]
        
        pq = [(grid[0][0], 0, 0)]
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while pq:
            curr = heapq.heappop(pq)

            if visited[curr[1]][curr[2]] < float('inf'):
                continue
            visited[curr[1]][curr[2]] = min(curr[0], visited[curr[1]][curr[2]])
            
            for i, j in dirs:

                i, j = curr[1] + i, curr[2] + j

                if i>=0 and j>=0 and i<n and j<m and visited[i][j] == float('inf'):
                    heapq.heappush(pq, (max(grid[i][j], curr[0]), i, j))
        
        return visited[-1][-1]
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(heights), len(heights[0])

        pacific, atlantic = [[0]*n for _ in range(m)], [[0]*n for _ in range(m)]
        pq, aq = [], []

        for i in range(m):
            pacific[i][0] = 1
            pq.append([i, 0])
            atlantic[i][n-1] = 1
            aq.append([i, n-1])
        
        for j in range(n):
            pacific[0][j] = 1
            pq.append([0, j])
            atlantic[m-1][j] = 1
            aq.append([m-1, j])

        while pq:
            i, j = pq.pop(0)
            
            for dirs in directions:
                a, b = i+dirs[0], j+dirs[1]

                if a>=0 and b>=0 and a<m and b<n and heights[a][b] >= heights[i][j] and pacific[a][b] == 0:
                    pacific[a][b] = 1
                    pq.append([a, b])
        
        while aq:
            i, j = aq.pop(0)
            
            for dirs in directions:
                a, b = i+dirs[0], j+dirs[1]

                if a>=0 and b>=0 and a<m and b<n and heights[a][b] >= heights[i][j] and atlantic[a][b] == 0:
                    atlantic[a][b] = 1
                    aq.append([a, b])
        
        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] == 1 and atlantic[i][j] == 1:
                    res.append([i, j])
        
        return res
        
        

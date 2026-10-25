class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        dist, n = defaultdict(list), len(points)

        for i in range(n):
            for j in range(i+1, n):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dist[i].append((j, cost))
                dist[j].append((i, cost))
    
        pq, visited = [(0, 0)], [False for _ in range(n)]
        cost = 0

        while pq:
            curr = heapq.heappop(pq)

            if visited[curr[1]]:
                continue
            
            visited[curr[1]] = True
            cost += curr[0]

            for neighbor in dist[curr[1]]:
                
                if visited[neighbor[0]]:
                    continue
                
                heapq.heappush(pq, (neighbor[1], neighbor[0]))
        
        return cost
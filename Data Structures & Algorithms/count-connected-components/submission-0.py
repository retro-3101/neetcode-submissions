class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = [False for _ in range(n)]

        adj = [[] for _ in range(n)]

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        count = 0

        while not all(visited):
            count+=1

            q = []

            for i, val in enumerate(visited):
                if not val:
                    q.append(i)
                    break

            while q:
                curr = q.pop(0)

                if visited[curr]:
                    continue
                
                visited[curr] = True

                for node in adj[curr]:
                    q.append(node)
        
        return count
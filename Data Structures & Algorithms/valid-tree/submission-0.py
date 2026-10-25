class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n-1:
            return False
        
        adj = [[] for _ in range(n)]
        visited = [False for _ in range(n)]

        for nodes in edges:
            adj[nodes[0]].append(nodes[1])
            adj[nodes[1]].append(nodes[0])

        q = []
        q.append(0)

        while q:
            curr = q.pop(0)

            if visited[curr]:
                continue
            
            visited[curr] = True
            
            for node in adj[curr]:
                q.append(node)
        

        return all(visited)

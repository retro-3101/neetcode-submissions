class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indeg = [0 for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]

        for node in prerequisites:
            adj[node[1]].append(node[0])
            indeg[node[0]]+=1
        
        q = []
        for i, val in enumerate(indeg):
            if not val:
                q.append(i)
        
        taken = 0
        while q:
            node = q.pop(0)
            taken += 1

            for neighbors in adj[node]:
                indeg[neighbors] -= 1

                if indeg[neighbors] == 0:
                    q.append(neighbors)
            
        return True if taken==numCourses else False    

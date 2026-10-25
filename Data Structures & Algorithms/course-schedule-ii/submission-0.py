class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indeg = [0 for i in range(numCourses)]
        adj = [[] for i in range(numCourses)]
        visited = [False for i in range(numCourses)]

        res = []

        for course in prerequisites:
            indeg[course[0]] += 1
            adj[course[1]].append(course[0])
        
        q = []

        for i, val in enumerate(indeg):
            if not val:
                q.append(i)
                visited[i] = True
        
        while q:
            curr = q.pop(0)
            res.append(curr)

            for course in adj[curr]:
                indeg[course]-=1

                if not indeg[course] and not visited[course]:
                    q.append(course)
                    visited[course] = True
        
        if len(res) == numCourses:
            return res
        
        return []
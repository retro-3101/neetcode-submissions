"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        copy = {}

        visited = set()
        if not node:
            return None
        copy[node] = Node(node.val)

        q = [node]

        while q:
            curr = q.pop(0)

            for neighbor in curr.neighbors:

                if neighbor not in visited:
                    copy[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                    visited.add(neighbor)
                
                copy[curr].neighbors.append(copy[neighbor])
        
        return copy[node]
            

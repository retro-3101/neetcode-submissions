# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 1
        if not root:
            return 0
        
        queue = []
        queue.append((root, 1))

        while queue:
            node = queue[0]
            max_depth = max(node[1], max_depth)
            queue.pop(0)

            if node[0].left:
                queue.append((node[0].left, node[1]+1))
            
            if node[0].right:
                queue.append((node[0].right, node[1]+1))
        
        return max_depth


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self, dist=0):
        self.dist = 0

    def helper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_dist = self.helper(root.left)
        right_dist = self.helper(root.right)

        self.dist = max(self.dist, left_dist + right_dist)

        return max(left_dist, right_dist) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        depth = self.helper(root)

        return self.dist
        
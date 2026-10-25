# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        lft_depth = self.helper(root.left)
        rgt_depth = self.helper(root.right)

        if(abs(lft_depth - rgt_depth) > 1):
            self.truth = False
        
        return max(lft_depth, rgt_depth) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.truth = True

        depth = self.helper(root)

        return self.truth
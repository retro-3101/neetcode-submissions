# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max_sum = root.val
        self.helper(root)

        return self.max_sum
    
    def helper(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        lft_sum = max(0, self.helper(root.left))
        rgt_sum = max(0, self.helper(root.right))

        curr_sum = root.val + lft_sum + rgt_sum

        self.max_sum = max(curr_sum, self.max_sum)

        return root.val + max(lft_sum, rgt_sum)
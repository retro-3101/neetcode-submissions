# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.count = k
        self.res = None

        self.helper(root)

        return self.res
    
    def helper(self, root: Optional[TreeNode]) -> None:

        if not root:
            return
        
        self.helper(root.left)

        if self.count:
            self.count -= 1
            self.res = root.val
        
        self.helper(root.right)

        return
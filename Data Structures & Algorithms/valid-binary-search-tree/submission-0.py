# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.helper(root, float('inf'), -float('inf'))
    
    def helper(self, root: Optional[TreeNode], mx: int, mn: int) -> bool:

        if not root:
            return True
        
        tmp = root.val

        if tmp >= mx or tmp<= mn:
            return False
        
        return self.helper(root.left, tmp, mn) and self.helper(root.right, mx, tmp)


        

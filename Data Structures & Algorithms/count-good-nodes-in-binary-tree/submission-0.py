# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 1

        self.helper(root.left, root.val)
        self.helper(root.right, root.val)

        return self.count

    def helper(self, root: TreeNode, maxval: int) -> None:
        if not root:
            return
        
        if root.val >= maxval:
            self.count += 1
        
        maxval = max(root.val, maxval)

        self.helper(root.left, maxval)
        self.helper(root.right, maxval)

        return
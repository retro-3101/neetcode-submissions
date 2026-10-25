# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.i_idx = { val: idx for idx, val in enumerate(inorder)}
        self.p_idx = 0
        self.preorder = preorder

        return self.helper(0, len(self.preorder) - 1)
    
    def helper(self, l: int, r: int) -> Optional[TreeNode]:

        if l>r:
            return None
        
        root = TreeNode(self.preorder[self.p_idx])
        self.p_idx += 1
        mid = self.i_idx[root.val]

        root.left = self.helper(l, mid-1)
        root.right = self.helper(mid+1, r)

        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lca = None
        self.p = p
        self.q = q

        finder = self.helper(root)

        return self.lca

    
    def helper(self, root: Optional[TreeNode]) -> List[bool]:
        
        truth = [False, False]
        if not root:
            return truth
        
        if root.val == self.p.val:
            truth[0] = True
        
        if root.val == self.q.val:
            truth[1] = True
        
        left_truth = self.helper(root.left)
        right_truth = self.helper(root.right)

        truth[0] = truth[0] or left_truth[0] or right_truth[0]
        truth[1] = truth[1] or left_truth[1] or right_truth[1]

        if truth[0] and truth[1] and self.lca is None:
            
            self.lca = root
        
        return truth
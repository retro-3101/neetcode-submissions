# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.sametree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sametree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        rq, sq = [root], [subRoot]

        while rq and sq:

            rnode, snode = rq[0], sq[0]
            rq.pop(0)
            sq.pop(0)

            if not rnode and not snode:
                continue
            
            if not rnode or not snode:
                return False

            if rnode.val != snode.val:
                return False
            
            rq.append(rnode.left)
            rq.append(rnode.right)
            sq.append(snode.left)
            sq.append(snode.right)
        
        return not sq and not rq
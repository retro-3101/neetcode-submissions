# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        q = [root]

        while q:
            lenq = len(q)
            temp = []

            for i in range(lenq):

                node = q[0]
                q.pop(0)
                temp.append(node.val)

                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            
            if temp:
                res.append(temp[0])
        
        return res
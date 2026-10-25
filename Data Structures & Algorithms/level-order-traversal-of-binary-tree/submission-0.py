# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        q = [[root, 1]]
        lvl = 1
        temp = []
        result = []

        while q:
            node = q[0]
            q.pop(0)

            if node[1] != lvl:
                lvl = node[1]
                result.append(temp)
                temp = []
            
            temp.append(node[0].val)

            if node[0].left:
                q.append([node[0].left, node[1]+1])
            
            if node[0].right:
                q.append([node[0].right, node[1]+1])

        if temp:
            result.append(temp)

        return result
            
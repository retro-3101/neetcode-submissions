# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pqueue, qqueue = [p], [q]

        while pqueue and qqueue:
            pnode = pqueue.pop(0)
            qnode = qqueue.pop(0)

            if not pnode and not qnode:
                continue
            if not pnode or not qnode:
                return False
            if pnode.val != qnode.val:
                return False

            pqueue.append(pnode.left)
            pqueue.append(pnode.right)
            qqueue.append(qnode.left)
            qqueue.append(qnode.right)

        return not pqueue and not qqueue  # ensure both queues are empty

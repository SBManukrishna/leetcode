# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res=[]
        q = deque([root])
    
        while q:
            q2 = deque()
            level = []
            while q:
                node = q.popleft() 
                level.append(node.val)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)

            res.append(level[-1])
            q=q2

        return res
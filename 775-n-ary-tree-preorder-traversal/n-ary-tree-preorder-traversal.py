"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res=[]
        def helper(root):
            if root==None:
                return
            res.append(root.val)
            for i in range(len(root.children)):
                helper(root.children[i])
        helper(root)        
        return res       


        
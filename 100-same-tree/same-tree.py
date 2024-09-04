# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res1=[]
        res2=[]
        def preorder(root,res):
            if(root==None):
                res.append("None")  
                return  
            res.append(root.val)
            preorder(root.left,res)
            preorder(root.right,res)    

        preorder(p,res1)
        preorder(q,res2)
        if(res1==res2):
            return True
        return False    

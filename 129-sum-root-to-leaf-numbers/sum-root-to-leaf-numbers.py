# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res=[]
        global sum
        sum=0
        def helper(root):
            res.append(root.val)
            global sum
            if(root.left==None and root.right==None):
                sum+=int((''.join(map(str,res))))
                res.pop()
                return
            if(root.left!=None):
                helper(root.left)
            if(root.right!=None):
                helper(root.right)
            res.pop()
        helper(root)     
        return sum          
       
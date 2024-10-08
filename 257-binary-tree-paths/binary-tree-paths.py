# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=[]
        new=[]
        s=""
        def helper(root):
            res.append(root.val)
            if(root.left==None and root.right==None):
                new.append("->".join(map(str,res)))
                res.pop()                
                return

            if(root.left!=None):
                helper(root.left)

            if(root.right!=None):
                helper(root.right)

            res.pop()        
        helper(root)  
        return new          

        
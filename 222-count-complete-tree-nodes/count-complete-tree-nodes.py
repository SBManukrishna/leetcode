# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        c=0
        def inorder(root,count):
            if root==None:
                return count
            count+=1
            count=inorder(root.left,count)
            count=inorder(root.right,count)
            return count    
        return inorder(root,0)    
        
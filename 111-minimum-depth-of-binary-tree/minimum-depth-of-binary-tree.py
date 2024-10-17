# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if(root==None):
            return 0

        def depth(root):
            if root.left and root.right:
                return  min(depth(root.left),depth(root.right))+ 1
            if root.left:
                return depth(root.left) + 1
            if root.right:
                return depth(root.right) + 1
            return 1

        return depth(root)
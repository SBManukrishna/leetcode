# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if(root == None):
        #     return 0

        # def helper(root):
        #     if root.left==None and root.right==None:
        #         return 1

        #     lDepth = 1
        #     rDepth = 1

        #     if(root.left!=None):
        #         lDepth += helper(root.left)

        #     if(root.right!=None):
        #         rDepth += helper(root.right)

        #     return max(lDepth, rDepth)
                  
        # return helper(root)  

        if(root == None):
            return 0
        global d,count
        d=0
        count=0
        def helper(root):
            global count
            count+=1
            print(f"{root.val} , {count}\n")

            if root.left==None and root.right==None:
                global d
                d=max(d, count)
                count-=1
                return

            if(root.left!=None):
                helper(root.left)

            if(root.right!=None):
                helper(root.right)

            count -= 1
        helper(root)
        return d           
        

        
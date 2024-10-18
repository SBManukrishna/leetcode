# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        res=[[root.val]]
        q=[root]

        while(True):
            que=[]
            while(len(q)!=0):
                item=q.pop(0)
                if(item.left!=None):
                    que.append(item.left)
                if(item.right!=None):
                    que.append(item.right)      
            if(len(que)==0):
                return res[::-1]
            res.append(list(map(lambda node:node.val,que)))
            q=que

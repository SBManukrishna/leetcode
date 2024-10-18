# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []

        res=[[root.val]]
        q=[root]
        isEven=True

        while len(q):
            que=[]
            ans=[]
            while(len(q)!=0):
                item=q.pop(0)

                if(item.left!=None):
                    que.append(item.left)
                    ans.append(item.left.val)

                if(item.right!=None):
                    que.append(item.right)
                    ans.append(item.right.val)
    
            if isEven:
                ans.reverse()    
                isEven=False
            else:
                isEven=True

            if len(ans):
                res.append(ans)
                q=que  
    
        return res       
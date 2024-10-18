# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q=[root]
        res=[float(root.val)]

        while(True):
            count=0
            sum=0
            que=[]
            while(len(q)!=0):
                item=q.pop(0)
                if(item.left!=None):
                    que.append(item.left)
                    sum+=item.left.val
                    count+=1
                if(item.right!=None):
                    que.append(item.right)
                    sum+=item.right.val
                    count+=1             
            if count==0:
                return res          
            res.append(sum/count)
            q=que
        




        
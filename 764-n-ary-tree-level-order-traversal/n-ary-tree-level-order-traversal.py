"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root==None:
            return []
        q=[root]
        res=[[root.val]]

        while(True):
            que=[]
            while(len(q)!=0):
                item=q.pop(0)
                for i in range(len(item.children)):
                    if item.children[i]!=None:
                        que.append(item.children[i])
            if(len(que)==0):
                return res
            res.append(list(map(lambda x: x.val,que)))
            q=que
        return res        
        

        
class Solution:
    def isValid(self, s: str) -> bool:
        v=[]
        d={'(':')','{':'}','[':']'}
        for i in s:
            if(i=='[' or i=='{' or i=='('):
                v.append(i)
            else:
                if v==[] or i!=d[v[-1]]:
                    return False
                else:
                    v.pop()
        if(v!=[]):
            return False
        return True                                 
            
        
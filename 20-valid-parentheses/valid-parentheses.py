class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        n=len(s)
        d={'(':')','{':'}','[':']'}
        if(s[0] in ['}',')',']']):
            return False
        for i in range(n):
            if(s[i] in ['(','{','[']):
                stack.append(s[i])
            else:
                if(len(stack)==0 or d[stack[len(stack)-1]]!=s[i]):
                    return False
                else:
                    stack.pop()  
        if stack==[]:
            return True
        return False                       
        
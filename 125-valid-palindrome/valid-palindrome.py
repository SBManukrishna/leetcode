class Solution:
    def isPalindrome(self, s: str) -> bool:
        d=""
        for i in s:
            if i.isalnum()==True:
                d+=i.lower()
        n=len(d)//2        
        for i in range(n):             
            if d[i]!=d[-1-i]:
                return False
        return True    
        
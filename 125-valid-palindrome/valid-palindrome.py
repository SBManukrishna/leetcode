class Solution:
    def isPalindrome(self, s: str) -> bool:
        d=""
        for i in s:
            if i.isalnum()==True:
                d+=i.lower()
        for i in range(len(d)//2):             
            if d[i]!=d[-1-i]:
                return False
        return True    
        
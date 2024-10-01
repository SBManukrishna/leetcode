class Solution:
    def isPalindrome(self, s: str) -> bool:
        d=""
        for i in s:
            if i.isalnum()==True:
                d+=i.lower()     
        if d==d[::-1]:
            return True
        False    
        
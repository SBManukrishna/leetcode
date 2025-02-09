class Solution:
    def longestPalindrome(self, s: str) -> str:
        sub=""
        max=0
        n=len(s)
        
        for i in range(len(s)):
            left=i
            right=i
            while(left>-1 and right<n and s[left]==s[right]):
                if (right+1-left)>max:
                    sub=s[left:right+1]
                    max=len(sub)
                left-=1
                right+=1        

            left=i
            right=i+1
            while(left>-1 and right<n and s[left]==s[right]):
                if (right+1-left)>max:
                    sub=s[left:right+1]
                    max=len(sub)
                left-=1
                right+=1  
        return sub        
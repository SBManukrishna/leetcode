class Solution:
    def fib(self, n: int) -> int:
        prev2=0
        prev=1
        if(n<=1):
            return n
        for i in range(2,n+1):
            curr=prev+prev2
            prev2=prev
            prev=curr   
        return curr  
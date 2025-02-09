class Solution:
    def fib(self, n: int) -> int:
        first=0
        second=1
        third=1
        if n==0:
            return 0
        for i in range(n-1):
            third=first+second
            first=second
            second=third
        return third    
            
        
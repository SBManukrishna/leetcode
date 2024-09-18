class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if(dividend==divisor):
            return 1
        sign=True
        if((dividend<0 and divisor>0) or (dividend>0 and divisor<0)):
            sign=False
        a=abs(dividend)
        b=abs(divisor)
        ans=0
        while(a>=b):
            count=0
            while(a>b<<(count+1)):
                count+=1
            ans+=1<<count
            a-=b<<count
        if(ans>=2**31 and sign==True):
            return 2**31-1
        if(ans>2**31 and sign==False):
            return  0-2**31
        if(sign==True):
            return ans
        return 0-ans                

        
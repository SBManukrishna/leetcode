class Solution:
    def bulbSwitch(self, n: int) -> int:
        return math.floor(math.sqrt(n))

        # if(n==0):
        #     return 0
        # if(n==1):
        #     return 1    
        # r=1
        # i=0
        # bulbs=[1]*n
        # while(r<n):
        #     r+=1
        #     for i in range(r-1,n,r):
        #         bulbs[i]=bulbs[i]^1 
        #     print(bulbs)     
        # return bulbs.count(1)        
        
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        l1=list(set(nums))
        count=0
        d=defaultdict(int)
        for i in l1:
            t1,t2=i+k,i-k
            if t1 in d:
                count+=d[t1]
            if t2 in d:
                count+=d[t2]  
            d[i]+=1
        if(k==0):
            t=defaultdict(int)
            for i in nums:
                t[i]+=1
            count=0
            for i in t:
                if(t[i]>=2):
                    count+=1    
        return count          
        
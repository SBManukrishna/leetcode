class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds=defaultdict(int)
        dt=defaultdict(int)
        for i in s:
            ds[i]+=1
        for i in t:
            dt[i]+=1
        if(ds==dt):
            return True
        return False        
        
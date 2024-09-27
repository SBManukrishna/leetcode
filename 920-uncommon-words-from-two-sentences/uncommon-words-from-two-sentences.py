class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d=defaultdict(int)
        s=(s1+" "+s2).split()
        for i in s:
            d[i]+=1
        res=[]    
        for i in d:
            if(d[i]==1):
                res.append(i)
        return res
        
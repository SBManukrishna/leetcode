class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a=sorted(list(set(arr)))
        d=defaultdict(int)
        k=1
        for i in a:
            d[i]=k
            k+=1
        res=[]    
        for i in arr:
            res.append(d[i])
        return res
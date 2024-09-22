class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            key="".join(sorted(i))
            if key in d:
                d[key]+=[i]
            else:
                d[key]=[i] 
        res=[]
        for i in d:
            res.append(list(d[i]))
        return res          
        
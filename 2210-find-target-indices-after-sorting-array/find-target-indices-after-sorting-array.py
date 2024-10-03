class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return []
        nums.sort()
        d={}
        index=0
        for i in nums:
            if i in d:
                d[i].append(index)
            else:
                d[i]=[index]
            index+=1    
        return d[target]

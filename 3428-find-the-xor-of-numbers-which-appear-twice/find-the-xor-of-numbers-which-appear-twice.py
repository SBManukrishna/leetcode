class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        d={}
        if(list(set(nums))==nums):
            return 0
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        xor=0
        for i in d:
            if d[i]==2:
                xor^=i
        return xor            
        
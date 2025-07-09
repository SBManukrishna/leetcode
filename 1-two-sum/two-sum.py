class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        d={}
        for i in range(n):
            d[nums[i]]=i
        for i in range(n):
            y=target-nums[i]
            if y in d and d[y]!=i:
                return [i,d[y]]    

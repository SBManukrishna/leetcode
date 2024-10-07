class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        n=len(nums)
        for i in range(n):
            d[i]=target-nums[i]
        for i in range(n):
            if d[i] in nums and i!=nums.index(d[i]):
                return [i,nums.index(d[i])]    
        